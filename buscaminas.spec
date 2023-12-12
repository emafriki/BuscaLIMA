# specfile.spec

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['buscaminas.py'],
             pathex=['C:\\Users\\Alma\\Desktop\\Codigos de etapa'],
             binaries=[],
             datas=[
                 ('img//bomba.ico', 'img'),    # Cambia las rutas según la ubicación de tus imágenes
                 ('img//banderaSlot.png', 'img'),
                 ('img//imagenTransparente.png', 'img'),
                 ('img//bomba3.png', 'img'),
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='buscaminas',
          debug=False,
          bootloader_ignore_signals=False,
          bootloader_blacklist_flags=[],
          runtime_tmpdir=None,
           console=False , icon='img//bomba.ico' )
