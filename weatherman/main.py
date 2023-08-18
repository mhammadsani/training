from weatherman_parser import parse_arguments
from weather import run_task, read_files


def main() -> None:
    if __name__ == "__main__":
        args = parse_arguments()
        read_files(args.weatherman_files_path)
        run_task(args)
main()
