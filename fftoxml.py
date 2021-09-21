#!/usr/bin/env python

import argparse
import xml.etree.ElementTree as ET


def indent_xml(elem, level=0, hor=' ', ver='\n'):
    '''pretty-print xml tree'''

    spc = ver + level * hor
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = spc + hor
        if not elem.tail or not elem.tail.strip():
            elem.tail = spc
        for elem in elem:
            indent_xml(elem, level + 1, hor, ver)
        if not elem.tail or not elem.tail.strip():
            elem.tail = spc
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = spc


class forcefield(object):
    '''force field parameter database'''

    def __init__(self, filename):

        self.ftree = ET.ElementTree(ET.Element('ForceField'))
        root = self.ftree.getroot()

        for line in open(filename, 'r'):
            if line.startswith('#') or line.strip() == '':
                continue
        
            if line.lower().startswith('atom'):
                section = 'atoms'
                atoms = ET.SubElement(root, 'Atoms')
                continue
            elif line.lower().startswith('bond'):
                section = 'bonds'
                bonds = ET.SubElement(root, 'Bonds')
                continue
            elif line.lower().startswith('angl'):
                section = 'angles'
                angles = ET.SubElement(root, 'Angles')
                continue
            elif line.lower().startswith('dihe'):
                section = 'dihedrals'
                dihedrals = ET.SubElement(root, 'Dihedrals')
                continue
            elif line.lower().startswith('impro'):
                section = 'improper'
                improper = ET.SubElement(root, 'Improper')
                continue
            tok = line.strip().split()
            if section == 'atoms':
                at = ET.SubElement(atoms, 'Atom')
                at.set('type', tok[0])
                at.set('class', tok[1])
                at.set('mass', str(tok[2]))
                at.set('charge', str(tok[3]))
                at.set('potential', tok[4])
                at.set('sigma', str(tok[5]))
                at.set('epsilon', str(tok[6]))
            elif section == 'bonds':
                bd = ET.SubElement(bonds, 'Bond')
                bd.set('class1', tok[0])
                bd.set('class2', tok[1])
                bd.set('potential', tok[2])
                bd.set('length', str(tok[3]))
                bd.set('k', str(tok[4]))
            elif section == 'angles':
                an = ET.SubElement(angles, 'Angles')
                an.set('class1', tok[0])
                an.set('class2', tok[1])
                an.set('class3', tok[2])
                an.set('potential', tok[3])
                an.set('angle', str(tok[4]))
                an.set('k', str(tok[5]))
            elif section == 'dihedrals':
                di = ET.SubElement(dihedrals, 'Dihedrals')
                di.set('class1', tok[0])
                di.set('class2', tok[1])
                di.set('class3', tok[2])
                di.set('class4', tok[3])
                di.set('potential', tok[4])
                di.set('v1', str(tok[5]))
                di.set('v2', str(tok[6]))
                di.set('v3', str(tok[7]))
                di.set('v4', str(tok[8]))
            elif section == 'improper':
                im = ET.SubElement(improper, 'Improper')
                im.set('class1', tok[0])
                im.set('class2', tok[1])
                im.set('class3', tok[2])
                im.set('class4', tok[3])
                im.set('potential', tok[4])
                im.set('v1', str(tok[5]))
                im.set('v2', str(tok[6]))
                im.set('v3', str(tok[7]))
                im.set('v4', str(tok[8]))

    def write(self, outfile):
        '''write force field to xml file'''

        indent_xml(self.ftree.getroot())
        self.ftree.write(outfile)


def main():
    parser = argparse.ArgumentParser(description =
        'convert force field file to xml',
        formatter_class = argparse.RawTextHelpFormatter)
    parser.add_argument('infile', help = 'force field file')
    parser.add_argument('outfile', help = 'output OpenMM xml file')
    args = parser.parse_args()

    ff = forcefield(args.infile)
    ff.write(args.outfile)


if __name__ == '__main__':
    main()
