# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['app.pyC:\\Users\\ZAKI\\AppData\\Local\\Programs\\Python\\Python38\\python.exe', 'c:/Developing/App/Python/Jadwal/app.py'],
             pathex=['C:\\Developing\\App\\Python\\Jadwal'],
             binaries=[],
             datas=[('data.json', '.')],
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
          name='python',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )