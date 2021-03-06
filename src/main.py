#          main.py file of catlang
#    Copyright (C) 2019  Dante Falzone
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import preprocessor as pp
import sys


# If an input file name foo.cat is preprocessed, we'll get
# out a file named foo.pp.c.
def main():
    input_file = open(sys.argv[1], "r").read().split('\n')
    output_file = open(sys.argv[1].replace('.', ".pp.").replace(".cat", ".c"), "w+")
    output_file.write("// Generated by the preprocessor for the C@ language\n")
    for line in input_file:
        if "pure " in line:
            output_file.write(pp.preproc_pure_func(line) + '\n')
        else:
            output_file.write(line + '\n')
    output_file.close()


if __name__ == "__main__":
    main()