# 0x17. Web stack debugging #3

## Description

This project focuses on debugging a web stack using `strace`. `strace` is a powerful command-line tool that allows you to trace system calls and signals. By analyzing the output of `strace`, you can identify and fix issues in your web stack.

## Objectives

- Understand the basics of web stack debugging.
- Learn how to use `strace` to trace system calls and signals.
- Analyze `strace` output to identify and fix issues in a web stack.
- Gain hands-on experience in debugging real-world web applications.

## Requirements

- Linux-based operating system (e.g., Ubuntu, CentOS).
- Basic knowledge of web development and server administration.
- Familiarity with command-line tools and terminal usage.  
  
## Usage

**To debug the web stack using `strace`, follow these steps:**

1. Open a terminal and navigate to the project directory.
2. Start the application: `python app.py` or `npm start`.
3. Open another terminal window and navigate to the project directory.
4. Run `strace` with the appropriate options: `strace -p <pid> -o <output_file>`.
5. Interact with the application to trigger the issue you want to debug.
6. Stop `strace` by pressing `Ctrl+C`.
7. Analyze the output file generated by `strace` to identify the issue.
8. Fix the issue in your web stack code.
9. Repeat steps 2-8 until all issues are resolved.

## Resources

- [Official `strace` documentation](https://strace.io/)
- [Debugging web applications with `strace`](https://www.linuxjournal.com/content/debugging-web-applications-strace)

## License

This project is licensed under the [MIT License](LICENSE).
