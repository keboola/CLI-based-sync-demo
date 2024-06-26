import argparse
import json
import logging
import os
import zipfile
from pathlib import Path

from storage_diff import StorageDiff as Diff, DiffToMarkdown

KEY_ORIGIN_SOURCE = "source"
KEY_ORIGIN_DESTINATION = "destination"

REPORT_FILE = "Storage_report.md"


class ProjectFile:
    project: str
    path: str

    def __init__(self, project, path):
        self.project = project
        self.path = path


class ComparisonStructure:
    environment: str
    projects: list[ProjectFile]

    def __init__(self):
        self.environment: str = ''
        self.projects: list[ProjectFile] = []

    def get_projects(self):
        return set(project.project for project in self.projects)

    def get_project(self, project):
        for p in self.projects:
            if p.project == project:
                return p
        return None


class StorageDiff:
    source_structure: ComparisonStructure
    destination_structure: ComparisonStructure

    def __init__(self, workdir):
        workdir = self._check_workdir(workdir)
        self.source_structure, self.destination_structure = self._create_objects_from_structure(workdir)

        # check if same projects are in both structures
        if self.source_structure.get_projects() != self.destination_structure.get_projects():
            raise ValueError("Projects in source and destination structures do not match!")

        markdown_output = [f"# Storage comparison result \n\n",
                           f"## Comparison environments '{self.source_structure.environment}' "
                           f"vs '{self.destination_structure.environment}' \n\n"]
        for source_project in self.source_structure.projects:
            destination_project = self.destination_structure.get_project(source_project.project)

            logging.info(f"Comparing project {source_project.project} vs {destination_project.project}")

            diff_file_path = f"{source_project.project}_vs_{destination_project.project}.json"
            diff_file = Diff(source_project.path, destination_project.path, diff_file_path).compare()

            markdown_output.append(
                f"## Project '{source_project.project}' vs project '{destination_project.project}'\n\n")
            markdown_output.extend(DiffToMarkdown(diff_file).convert())

        self._write_report(markdown_output)

    @staticmethod
    def create_markdown(diff_file):
        logging.info(f"Translating diff file {diff_file} to markdown")
        with open(diff_file, 'r') as f:
            diff = json.load(f)

        if not diff:
            return ["### Storage structure is the same\n\nNo changes detected\n"]

        markdown_lines = []
        for event in diff:
            if event['event'] == 'ADD_BUCKET':
                markdown_lines.append(f"### Bucket added\n\n{event['bucket']}\n")
            elif event['event'] == 'DROP_BUCKET':
                markdown_lines.append(f"### Bucket removed\n\n{event['bucket']}\n")
            elif event['event'] == 'MODIFY_BUCKET':
                markdown_lines.append(f"### Bucket modified\n\n{event['bucket']}\n")
            elif event['event'] == 'ADD_TABLE':
                markdown_lines.append(f"### Table added\n\n{event['table']}\n")
            elif event['event'] == 'DROP_TABLE':
                markdown_lines.append(f"### Table removed\n\n{event['table']}\n")
            # TODO: Add more event types here...

        return markdown_lines

    @staticmethod
    def _write_report(markdown_output):
        with open(REPORT_FILE, 'w') as f:
            f.write('\n'.join(markdown_output))
        logging.info(f"Report written to {REPORT_FILE}")

    def _check_workdir(self, workdir):
        # check if workdir file exists
        if not os.path.exists(workdir):
            raise FileNotFoundError(f"Workdir file {workdir} not found")

        # check if workdir is a zip file unzip it
        if workdir.endswith('.zip'):
            workdir = self._unzip_dir(workdir)

        return workdir

    @staticmethod
    def _create_objects_from_structure(base_path):
        base_path = Path(base_path)
        source = ComparisonStructure()
        destination = ComparisonStructure()

        for origin_path in base_path.iterdir():
            if origin_path.is_dir():
                for env_path in origin_path.iterdir():
                    if env_path.is_dir():
                        env = env_path.name

                        for file_path in env_path.glob('*.json'):
                            proj = ProjectFile(file_path.stem, str(file_path))

                            if origin_path.name == KEY_ORIGIN_SOURCE:
                                if not source.environment:
                                    source.environment = env
                                source.projects.append(proj)
                            elif origin_path.name == KEY_ORIGIN_DESTINATION:
                                if not destination.environment:
                                    destination.environment = env
                                destination.projects.append(proj)

        return source, destination

    @staticmethod
    def _unzip_dir(workdir):
        # get the directory to extract the zip file and zip file_name
        extract_to = str(os.path.join(os.path.dirname(workdir), os.path.basename(workdir).split('.')[0]))
        if not os.path.exists(extract_to):
            os.makedirs(extract_to)
        with zipfile.ZipFile(workdir, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        return extract_to


def check_parameters():
    parser = argparse.ArgumentParser(description='Storage structure comparison')
    parser.add_argument('--workdir', type=str, required=True)
    return parser.parse_args()


if __name__ == '__main__':
    args = check_parameters()
    StorageDiff(
        workdir=args.workdir
    )
