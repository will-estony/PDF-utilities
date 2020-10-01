# pdf_splitter.py

import os
import sys

from PyPDF2 import PdfFileReader, PdfFileWriter


class Section(object):

    def __init__(self, num, num_pages, title=None):
        self.num = num
        self.num_pages = num_pages
        self.title = title

class Chapter(object):

    def __init__(self, num, num_sections, sections=[]):
        self.num = num
        self.num_sections = num_sections
        self.sections = sections
    
    def get_num_sections(self):
        return len(self.sections)

class Textbook(object):

    def __init__(self, title, start_page, num_chapters, chapters=[]):
        self.title = title
        self.start_page = start_page
        self.num_chapters = num_chapters
        self.chapters = chapters

def split_by_section(read_path, write_path, textbook):
    """
    Used when splitting up a textbook that has chapters AND sections within chapters
    """
    pdf_reader = PdfFileReader(read_path)
    
    
    page_num = textbook.start_page

    for chapter in textbook.chapters:
        for section in chapter.sections:
            pdf_writer = PdfFileWriter()
            for page in range(page_num, page_num + section.num_pages):
                pdf_writer.addPage(pdf_reader.getPage(page))
            
            output_filename = '{}.{}.pdf'.format(chapter.num, section.num)
            output_file_path = write_path + output_filename
            with open(output_file_path, 'wb') as out:
                pdf_writer.write(out)
                print('Created: {}'.format(output_filename))
            
            page_num = page_num + section.num_pages

def split_by_chapter(read_path, write_path, textbook):
    """
    Used when trying to split up a textbook with only chapters (no subsections)
    """
    pdf_reader = PdfFileReader(read_path)
    
    
    page_num = textbook.start_page

    for section in textbook.chapters:

        pdf_writer = PdfFileWriter()
        for page in range(page_num, page_num + section.num_pages):
            pdf_writer.addPage(pdf_reader.getPage(page))
        
        page_num = page_num + section.num_pages
        output_filename = '{}.pdf'.format(section.title)
        output_file_path = write_path + output_filename
        with open(output_file_path, 'wb') as out:
            pdf_writer.write(out)
            print('Created: {}'.format(output_filename))

def split_all_pages(read_path, write_path, start_page, end_page):
    """
    Used when trying to take every page in a pdf and save it as its own individual pdf file
    """
    pdf_reader = PdfFileReader(read_path)
    page_num = start_page
    for page in range(start_page, end_page + 1):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf_reader.getPage(page))
        output_filename = '{}.pdf'.format(page_num + 1)
        output_file_path = write_path + output_filename
        with open(output_file_path, 'wb') as out:
            pdf_writer.write(out)
            print('Created: {}'.format(output_filename))
        page_num = page_num + 1
        
    
def crop_pages(read_path, write_path, start_page, end_page, output_filename):
    pdf_reader = PdfFileReader(read_path)
    pdf_writer = PdfFileWriter()

    for page in range(start_page, end_page):
        pdf_writer.addPage(pdf_reader.getPage(page))

    output_file_path = write_path + output_filename
    with open(output_file_path, 'wb') as out:
        pdf_writer.write(out)
        print('Created: {}'.format(output_filename))

def combine_pages(read_path_1, read_path_2, write_path, output_filename):
    pdf_reader_1 = PdfFileReader(read_path_1)
    pdf_reader_2 = PdfFileReader(read_path_2)
    
    pdf_writer = PdfFileWriter()

    #add each page in the first pdf to the pdf writer
    for page in range(pdf_reader_1.getNumPages()):
        pdf_writer.addPage(pdf_reader_1.getPage(page))
    
    #add each page in the second pdf to the pdf write
    for page in range(pdf_reader_2.getNumPages()):
        pdf_writer.addPage(pdf_reader_2.getPage(page))

    output_file_path = write_path + output_filename
    with open(output_file_path, 'wb') as out:
        pdf_writer.write(out)
        print('Created: {}'.format(output_filename))

def add_page(read_pages_path, read_page_path, write_path, output_filename, insert_index):
    pdf_reader_1 = PdfFileReader(read_pages_path)
    pdf_reader_2 = PdfFileReader(read_page_path)
    
    pdf_writer = PdfFileWriter()

    for page in range(insert_index):
        pdf_writer.addPage(pdf_reader_1.getPage(page))

    pdf_writer.addPage(pdf_reader_2.getPage(0))

    for page in range(insert_index, pdf_reader_1.getNumPages()):
        pdf_writer.addPage(pdf_reader_1.getPage(page))

    output_file_path = write_path + output_filename
    with open(output_file_path, 'wb') as out:
        pdf_writer.write(out)
        print('Created: {}'.format(output_filename))

def pdf_to_text(file_path, start_page, end_page):
    pass


read_path = '/Users/williamestony/Desktop/InformationSecurityPrinciplesandPractice.pdf'
write_path = '/Users/williamestony/Desktop/'


pdf_reader = PdfFileReader(read_path)
pdf_writer = PdfFileWriter()
page_num = 42
for page in range(page_num, 73):
    pdf_writer.addPage(pdf_reader.getPage(page))

output_filename = '2.pdf'
output_file_path = write_path + output_filename
with open(output_file_path, 'wb') as out:
    pdf_writer.write(out)
    print('Created: {}'.format(output_filename))




