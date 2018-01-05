from generator import ConfigGenerator, ConfigFileError
import click


@click.command()
@click.option('--config_file', default='config.ini', help='config_file.')
def main(config_file):
    if config_file:
        try:
            ConfigGenerator(config_file=config_file)
        except ConfigFileError as e:
            print(e)


if __name__ == "__main__":
    main()
