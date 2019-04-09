"""main """
import click

from .generator.config_generator import ConfigGenerator, ConfigFileError


@click.command()
@click.option('--config_file', default='config.ini', help='config_file.')
def main(config_file):
    """main"""
    if config_file:
        try:
            ConfigGenerator(config_file=config_file)
        except ConfigFileError as exc:
            print(exc)


if __name__ == "__main__":
    main()
