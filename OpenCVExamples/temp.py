"""A cli group command cannot run options by itself"""
import click
import cv2


class Configuration(object):
    """context class

    I get the `criteria
    <http://opencv-python-tutroals.readthedocs.org/en/latest/
    py_tutorials/py_calib3d/py_calibration/py_calibration.html>`_
    from a tutorial.

    There is a brief discussion of the `criteria
    <http://docs.opencv.org/master/d9/d5d/
    classcv_1_1TermCriteria.html#gsc.tab=0>`_
    that says the following for each of the three parameters:

    type        The type of termination criteria, one of TermCriteria::Type
    maxCount    The maximum number of iterations or elements to compute.
    epsilon     The desired accuracy or change in parameters at which the
                iterative algorithm stops.
    """
    def __init__(self, criteria):
        """initialize criteriauration"""
        self.criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
                         30,
                         0.001)

    def __repr__(self):
        return '<ctx Configuration obj %r>' % self.criteria

pass_criteria = click.make_pass_decorator(Configuration)


@click.group()
@click.pass_context
def cli(ctx):
    """group cli for all commands"""
    ctx.obj = Configuration("this is a criteriauration")


@cli.command()
@click.pass_context
def print_criteria(ctx):
    click.echo(ctx.obj)
