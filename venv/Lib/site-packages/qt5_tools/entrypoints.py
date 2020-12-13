import functools
import os
import subprocess
import sys

import click
import qt5_applications

import qt5_tools


fspath = getattr(os, 'fspath', str)


@click.group()
def main():
    pass


def run(application_name, args=(), environment=os.environ):
    modified_environment = qt5_tools.create_environment(
        reference=environment,
    )
    application_path = qt5_applications._application_path(application_name)

    completed_process = subprocess.run(
        [
            fspath(application_path),
            *args,
        ],
        env=modified_environment,
    )

    return completed_process.returncode


# written by build.py

# @main.command(
#     add_help_option=False,
#     context_settings={
#         'ignore_unknown_options': True,
#         'allow_extra_args': True,
#     },
# )
# @click.pass_context
# def designer(ctx):
#     return run('designer', args=ctx.args)

# ----  start of generated wrapper entry points


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def assistant(ctx):
    return run('assistant', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def canbusutil(ctx):
    return run('canbusutil', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def designer(ctx):
    return run('designer', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def lconvert(ctx):
    return run('lconvert', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def licheck64(ctx):
    return run('licheck64', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def linguist(ctx):
    return run('linguist', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def lprodump(ctx):
    return run('lprodump', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def lrelease(ctx):
    return run('lrelease', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def lrelease_pro(ctx):
    return run('lrelease-pro', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def lupdate(ctx):
    return run('lupdate', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def lupdate_pro(ctx):
    return run('lupdate-pro', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def moc(ctx):
    return run('moc', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def pixeltool(ctx):
    return run('pixeltool', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qcollectiongenerator(ctx):
    return run('qcollectiongenerator', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qdbus(ctx):
    return run('qdbus', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qdbuscpp2xml(ctx):
    return run('qdbuscpp2xml', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qdbusviewer(ctx):
    return run('qdbusviewer', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qdbusxml2cpp(ctx):
    return run('qdbusxml2cpp', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qdistancefieldgenerator(ctx):
    return run('qdistancefieldgenerator', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qdoc(ctx):
    return run('qdoc', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qgltf(ctx):
    return run('qgltf', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qhelpgenerator(ctx):
    return run('qhelpgenerator', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qlalr(ctx):
    return run('qlalr', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmake(ctx):
    return run('qmake', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qml(ctx):
    return run('qml', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmlcachegen(ctx):
    return run('qmlcachegen', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmleasing(ctx):
    return run('qmleasing', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmlformat(ctx):
    return run('qmlformat', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmlimportscanner(ctx):
    return run('qmlimportscanner', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmllint(ctx):
    return run('qmllint', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmlmin(ctx):
    return run('qmlmin', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmlplugindump(ctx):
    return run('qmlplugindump', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmlpreview(ctx):
    return run('qmlpreview', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmlprofiler(ctx):
    return run('qmlprofiler', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmlscene(ctx):
    return run('qmlscene', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmltestrunner(ctx):
    return run('qmltestrunner', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmltyperegistrar(ctx):
    return run('qmltyperegistrar', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qscxmlc(ctx):
    return run('qscxmlc', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qtattributionsscanner(ctx):
    return run('qtattributionsscanner', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qtdiag(ctx):
    return run('qtdiag', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qtpaths(ctx):
    return run('qtpaths', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qtplugininfo(ctx):
    return run('qtplugininfo', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qtwaylandscanner(ctx):
    return run('qtwaylandscanner', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qvkgen(ctx):
    return run('qvkgen', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def rcc(ctx):
    return run('rcc', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def repc(ctx):
    return run('repc', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def sdpscanner(ctx):
    return run('sdpscanner', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def tracegen(ctx):
    return run('tracegen', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def uic(ctx):
    return run('uic', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def xmlpatterns(ctx):
    return run('xmlpatterns', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def xmlpatternsvalidator(ctx):
    return run('xmlpatternsvalidator', args=ctx.args)


# ----  end of generated wrapper subcommands

