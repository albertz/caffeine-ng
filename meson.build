project(
    'caffeine-ng',
    version: '4.1.0',
    meson_version: '>=0.63.0',
)

dependency('pygobject-3.0')
dependency('dbus-python')
dependency('gtk+-3.0')
dependency('libnotify')
dependency('indicator3-0.4')
dependency('appindicator3-0.1')
dependency('libxfconf-0', required: false)

pymod = import('python')
python = pymod.find_installation('python',
  modules: ['xdg', 'click', 'ewmh', 'setproctitle', 'pulsectl']
)
python.dependency()

prefix = get_option('prefix')
pkgdatadir = join_paths(prefix, get_option('datadir'))

# TODO: use pkgdatadir=/usr/share/caffeine
#       and only hardcode this base path into paths.py
localedir = join_paths(pkgdatadir, 'locale')
gladedir = join_paths(pkgdatadir, 'caffeine/glade')
imagedir = join_paths(pkgdatadir, 'caffeine/images')
iconsdir = join_paths(pkgdatadir, 'icons')

conf_data = configuration_data({
  'localedir': localedir,
  'gladedir': gladedir,
  'imagedir': imagedir,
  'iconsdir': iconsdir,
})

paths_py = configure_file(
    input: 'caffeine/paths.py',
    output: 'paths.py',
    configuration: conf_data,
)

# Cannot use vcs_tag; that file cannot be installed.
# See: https://github.com/mesonbuild/meson/issues/4893
version_py = configure_file(
    input: 'caffeine/version.py',
    output: 'version.py',
    configuration: configuration_data({
      'VCS_TAG': run_command('git', 'describe', '--long', '--tags', '--dirty', '--always').stdout().strip()
    }),
)

py_sources = [
    'caffeine/__init__.py',
    'caffeine/__main__.py',
    'caffeine/applicationinstance.py',
    'caffeine/cli.py',
    'caffeine/core.py',
    'caffeine/icons.py',
    'caffeine/inhibitors.py',
    'caffeine/main.py',
    paths_py,  # Is patched with locations.
    'caffeine/procmanager.py',
    'caffeine/triggers.py',
    'caffeine/utils.py',
    version_py,  # Is patched with VCS version.
]
python.install_sources(py_sources,
  subdir: 'caffeine',
)

install_data(
  'bin/caffeine',
  install_mode: 'rwxr-xr-x',
  install_dir: get_option('bindir'),
)

install_data(
  'share/applications/caffeine.desktop',
  install_dir: join_paths(get_option('sysconfdir'), 'xdg/autostart'),
)

install_data(
  'share/applications/caffeine.desktop',
  install_dir: join_paths(pkgdatadir, 'applications'),
)

subdir('translations')

install_man('share/man/man1/caffeine.1')

install_subdir('caffeine/assets/glade',
  install_dir: gladedir,
  strip_directory: true,
)

install_subdir('caffeine/assets/images',
  install_dir: imagedir,
  strip_directory: true,
)

install_subdir('caffeine/assets/icons',
  install_dir: iconsdir,
  strip_directory: true,
)

install_data(
  'share/glib-2.0/schemas/net.launchpad.caffeine.gschema.xml',
  install_dir: join_paths(pkgdatadir, 'glib-2.0/schemas/'),
)

install_data(
  './share/pixmaps/caffeine.png',
  install_dir: join_paths(pkgdatadir, 'pixmaps'),
)
