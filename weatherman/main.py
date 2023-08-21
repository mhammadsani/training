from weatherman_parser import parse_arguments, run_task, read_files


def main() -> None:
        args = parse_arguments()
        read_files(args.weatherman_files_path)
        run_task(args)

if __name__ == "__main__":
    main()
