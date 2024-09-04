#!/usr/bin/env python3
import subprocess
import os
import typer
import yaml
import sys 

app = typer.Typer(context_settings={"help_option_names": ["-h", "--help"]})

@app.command()
def run():
    # run the scripts/ folder and according to the name of the config
    setup()

@app.command()
def s():
    setup()

# Load the configuration
script_path = os.getenv('CLI_PATH', '')
with open(f"{script_path}/config.yml", "r") as config_file:
    config = yaml.safe_load(config_file)

# Loop through each command in the configuration
for command in config.get('commands', []):
    name = command.get('name')
    description = command.get('description', '')
    cmd_type = command.get('type', 'bash')

    def create_command(cmd_name, cmd_type):
        def generic_function(args: str = typer.Argument(None)):
            script_path = os.getenv('CLI_PATH', '') + "/dev/" + cmd_name
            if cmd_type == 'bash':
                full_command = [script_path] + (args.split() if args else [])
                try:
                    subprocess.run(full_command, check=True)
                except subprocess.CalledProcessError as e:
                    typer.echo(f"Error: Command '{' '.join(full_command)}' exited with {e.returncode}")
                    if e.stdout:
                        typer.echo("Output from the command:")
                        typer.echo(e.stdout)
                    if e.stderr:
                        typer.echo("Error output from the command:")
                        typer.echo(e.stderr)
                
            elif cmd_type == 'python':
                try:
                    exec(open(script_path).read(), globals())
                except Exception as e:
                    typer.echo(f"Error executing Python script: {e}")

        return generic_function

    # Dynamically create and add the command to the app
    app.command(name=name, help=description)(create_command(name, cmd_type))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        # If no arguments are provided, show help
        app(['--help'])
    else:
        app()

