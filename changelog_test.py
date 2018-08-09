"""Parses results of git commands to validate changelog was updated"""
# pylint: disable=no-member

import subprocess
import sys


def changelog_exists():
    """Check if changelog.md exists."""

    output = subprocess.getoutput(['ls'])
    return 'changelog.md' in output.lower()


def changelog_updated(target_branch):
    """Parse git diff to determine if changelog was updated."""

    output = subprocess.getoutput(['git diff HEAD origin/{}'.format(target_branch)])
    return 'a/changelog.md b/changelog.md' in output.lower()


def main():
    """Main function."""

    source_branch = sys.argv[1]
    print('source_branch:', source_branch)

    target_branch = sys.argv[2]
    print('target_branch:', target_branch)

    if not changelog_exists():
        raise Exception('Please add CHANGELOG.MD to this repo.')
    elif not changelog_updated(target_branch):
        raise Exception('CHANGELOG.MD must be updated for each pull request')


if __name__ == '__main__':
    main()
