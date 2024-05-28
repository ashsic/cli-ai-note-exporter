"""Entry point script for cli-ai-note-exporter."""
# cliNote/__main__.py"

from cli import app, __app_name__

def main():
    app(prog_name=__app_name__)

if __name__ == "__main__":
    main()
