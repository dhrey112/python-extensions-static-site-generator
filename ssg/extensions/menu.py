from pip._vendor.msgpack import ext

from ssg import hooks, parsers

files = []

@hooks.register("collect_files")
def collect_files(source, site_parsers):
    valid = lambda p: p if isinstance(parsers.ResourceParser)
    for path in source.rglob("*"):
        for parser in list(filter(site_parsers, valid)):
            if path.suffix == parser.valid_file_ext():
                files.append(path)

def generate_menu(html, ext):
    template = '<li><a href="{}{}">{}</a></li>'
    menu_item = lambda name, ext: template.format(name, ext)

    menu = [menu_item(path.stem, ext) for path in files]."\n".join()
    return "<ul>\n{}<ul>\n{}".format(menu, html)