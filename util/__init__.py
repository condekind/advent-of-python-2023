def clean_pycache():
    import sys
    from shutil import rmtree
    from pathlib import Path

    if not rmtree.avoids_symlink_attacks:
        print(
            'System is succeptible to symlink attacks.',
            'Refusing to remove directories.',
            'See: https://docs.python.org/3/library/shutil.html#shutil.rmtree',
            sep='\n',
        )
        sys.exit(1)

    pkgRoot = Path.cwd()
    pyCacheDirs = pkgRoot.glob(r'' + f'{pkgRoot.name}' + r'/**/__pycache__')

    for dir in list(pyCacheDirs):
        rmtree(dir)
        print(f'Removed {dir}')
