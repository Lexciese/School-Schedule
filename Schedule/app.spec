# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['app.py'],
             pathex=['C:\\Developing\\App\\Python\\Jadwal\\Schedule'],
             binaries=[],
             datas = [
                 ('C:\\Developing\\App\\Python\\Jadwal\\Data\\UserData.json', 'Data'),
                 ('C:\\Developing\\App\\Python\\Jadwal\\Data\\Help.txt', 'Data'),
                 ('C:\\Developing\\App\\Python\\Jadwal\\Data\\About.txt', 'Data'),
                 ('C:\\Developing\\App\\Python\\Jadwal\\Bin\\Images', 'Bin\\Images')
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
          [],
          exclude_binaries=True,
          name='Schedule',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Schedule')
