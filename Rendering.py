import sys
import os
import time
import subprocess

class Rendering:

    class PlanetMap:

        def __init__(self):
            self.list_map = []
            
            self.SCALES = {
                1: {'x': 50, 'y': 25, 'square_side': 10, 'resize_values': [60, 33], 'info': '500x500 Cells || 5x5 Sectors'},
                2: {'x': 55, 'y': 25, 'square_side': 5, 'resize_values': [60, 34], 'info': ':)'},
                3: {'x': 60, 'y': 36, 'square_side': 6,  'resize_values': [65, 44], 'info': ':('}
            }

            self.ConsoleResize(30, 60)

        def ConsoleResize(self, cols, rows):
            if sys.platform == 'linux':
                if 'xterm' in os.environ.get('TERM'):
                        os.system(f"resize -s {cols} {rows}")
                else:
                    os.system(f"stty cols {cols} rows {rows}")

                os.system('clear')

        def Clear(self):
            subprocess.run('clear')

        def DefineSizes(self, key):

            x = self.SCALES[key]['x']
            y = self.SCALES[key]['y']

            square_side = self.SCALES[key]['square_side']

            if square_side%2 != 0:
                y += 1

            return x, y, square_side
        
        def CreatingLines(self, length, square_side):

            up_line = ''
            base_line = ''
            none_line = ''
            down_line = ''

            for i in range(length):
                if i == 0:
                    continue

                if i%square_side == 0:
                    up_line += '┬'
                    base_line += '┼'
                    none_line += '│'
                    down_line += '┴'
                else:
                    up_line += '─'
                    base_line += '─'
                    none_line += ' '
                    down_line += '─'

            return up_line, base_line, none_line, down_line
        
        def CreatingList(self, height, square_side, up_line, base_line, none_line, down_line):

            self.list_map.append(list(f'┌{up_line}┐'))
            for i in range(height):
                if i == 0:
                    continue
                if i%(square_side//2) != 0:
                    self.list_map.append(list(f'│{none_line}│'))
                else:
                    self.list_map.append(list(f'├{base_line}┤'))

            self.list_map.append(list(f'└{down_line}┘'))

        def DrawClock(self):
            return f' ┌{"─"*26}┐\n │ {time.ctime()} │\n └{"─"*26}┘'

        
        def MapDraw(self, key):

            length, height, square_side = self.DefineSizes(key)

            self.ConsoleResize(self.SCALES[key]['resize_values'][1], self.SCALES[key]['resize_values'][0])

            up_line, base_line, none_line, down_line = self.CreatingLines(length, square_side)

            self.CreatingList(height, square_side, up_line, base_line, none_line, down_line)

            text_info = self.SCALES[key]["info"]

            while True:
                print(self.DrawClock())
                for i in self.list_map:
                    print(' '+''.join(i))

                print(f' ┌{"─"*(len(text_info)+8)}┐\n │ INFO: {text_info} │\n └{"─"*(len(text_info)+8)}┘')

        def PlanetRendering(self, key):
                while True:
                    self.Clear()
                    self.MapDraw(key)
                    time.sleep(1)