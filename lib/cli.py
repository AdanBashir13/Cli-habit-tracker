#!/usr/bin/env python3

import click
from helpers import (
    exit_program,
    list_users,
    create_user,
    update_user,
    delete_user,
    list_habits,
    create_habit,
    update_habit,
    delete_habit,
    list_habit_completions,
    create_habit_completion,
    update_habit_completion,
    delete_habit_completion
)

@click.group()
def cli():
    pass

@cli.command('exit-program')
def exit_cmd():
    exit_program()

@cli.command('list-users')
def list_users_cmd():
    list_users()

@cli.command('create-user')
def create_user_cmd():
    create_user()

@cli.command('update-user')
def update_user_cmd():
    update_user()

@cli.command('delete-user')
def delete_user_cmd():
    delete_user()

@cli.command('list-habits')
def list_habits_cmd():
    list_habits()

@cli.command('create-habit')
def create_habit_cmd():
    create_habit()

@cli.command('update-habit')
def update_habit_cmd():
    update_habit()

@cli.command('delete-habit')
def delete_habit_cmd():
    delete_habit()

@cli.command('list-habit-completions')
def list_habit_completions_cmd():
    list_habit_completions()

@cli.command('create-habit-completion')
def create_habit_completion_cmd():
    create_habit_completion()

@cli.command('update-habit-completion')
def update_habit_completion_cmd():
    update_habit_completion()

@cli.command('delete-habit-completion')
def delete_habit_completion_cmd():
    delete_habit_completion()

if __name__ == "__main__":
    cli()
