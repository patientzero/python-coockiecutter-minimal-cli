if __name__ == '__main__':
    from {{ cookiecutter.module_name }}.cli import cli, CLI_NAME
    cli(prog_name=CLI_NAME)
