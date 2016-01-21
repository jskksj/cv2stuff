import click


class configuration():
    def __init__(self, criteria)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
                30,
                0.001)

@click.command()
@click.argument('input', type=click.File('rb'), nargs=-1)
@click.argument('output', type=click.File('wb'))
def cli(input, output):
    """This script works similar to the Unix `cat` command but it writes
    into a specific file (which could be the standard output as denoted by
    the ``-`` sign).

    \b
    Copy stdin to stdout:
        inout - -

    \b
    Copy foo.txt and bar.txt to stdout:
        inout foo.txt bar.txt -

    \b
    Write stdin into the file foo.txt
        inout - foo.txt
    """
    for f in input:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            output.write(chunk)
            output.flush()
