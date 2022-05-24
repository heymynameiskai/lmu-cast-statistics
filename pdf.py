from fpdf import FPDF

data = {
    0: {
        'video': 'Vorlesung 1',
        'hits_online': 10,
        'hits_video': 4,
        'hits_audio': 0
    },
    1: {
        'video': 'Vorlesung 2',
        'hits_online': 10,
        'hits_video': 30,
        'hits_audio': 0
    },
    2: {
        'video': 'Vorlesung 3',
        'hits_online': 10,
        'hits_video': 4,
        'hits_audio': 1
    },
    3: {
        'video': 'Vorlesung 4',
        'hits_online': 100,
        'hits_video': 41,
        'hits_audio': 10
    }
}


def printPageHeader(pdf, playlist_title, playlist_url, date):
    pdf.set_font('Helvetica', 'B', 20)
    pdf.multi_cell(0, 8, playlist_title.encode("ascii", "ignore").decode(), align = 'L')
    pdf.ln()

    pdf.set_font('Helvetica', 'U', 10)
    pdf.set_text_color(0,0,255)
    pdf.cell(0, 6, playlist_url, link = playlist_url)
    pdf.ln(5)

    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.cell(0, 6, 'Stand: '+date)
    pdf.ln(15)

def printTableHeading(pdf):
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_fill_color(200, 200, 200)
    pdf.cell(115, 7, "Videotitel", 1, fill = True)
    pdf.cell(25, 7, "Online", 1, fill = True)
    pdf.cell(25, 7, "High Quality", 1, fill = True)
    pdf.cell(25, 7, "Audio", 1, fill = True)
    pdf.ln()

def printTableRow(pdf, name, online, video, audio):
    pdf.set_font('Helvetica', '', 10)
    # pdf.cell(110, 7, name, border = 'LR')
    # pdf.cell(25, 7, online, border = 'LR')
    # pdf.cell(25, 7, video, border = 'LR')
    # pdf.cell(25, 7, audio, border = 'LR')
    pdf.cell(115, 7, name, 1)
    pdf.cell(25, 7, online, 1)
    pdf.cell(25, 7, video, 1)
    pdf.cell(25, 7, audio, 1)
    pdf.ln()

def printLastRow(pdf):
    pdf.cell(115, 0, '', border = 'BLR')
    pdf.cell(25, 0, '', border = 'BLR')
    pdf.cell(25, 0, '', border = 'BLR')
    pdf.cell(25, 0, '', border = 'BLR')



def printStatistics(file_name, date, playlist_title, playlist_url, hits):
    pdf = FPDF()
    pdf.add_page()
    printPageHeader(pdf, playlist_title, playlist_url, date)
    printTableHeading(pdf)

    for i in sorted(hits.keys(), reverse=True):
        printTableRow(pdf, hits[i]['name'], str(hits[i]['hits_online']), str(hits[i]['hits_video']), str(hits[i]['hits_audio']))
    pdf.close()
    pdf.output((file_name.encode("ascii", "ignore").decode())+'.pdf')
    print("   ...exported")



# pdf.set_font('Helvetica', '', 12)
# pdf.multi_cell(40, 7, "headingheadingheading", border = 'LR', new_x='RIGHT', new_y='TOP')
# print(pdf.get_string_width("headingheadingheading"))
# pdf.multi_cell(40, 7, "heading", border = 'LR', new_x='RIGHT', new_y='TOP')
# pdf.multi_cell(40, 7, "heading", border = 'LR', new_x='RIGHT', new_y='TOP')
# pdf.ln(20)
# pdf.cell(40, 7, "heading", border = 'LR')
# pdf.cell(40, 7, "heading", border = 'LR')
# pdf.cell(40, 7, "heading", border = 'LR')
# pdf.ln()
# pdf.cell(40, 7, "heading", border = 'LR')
# pdf.cell(40, 7, "heading", border = 'LR')
# pdf.cell(40, 7, "heading", border = 'LR')
# pdf.ln()
# pdf.cell(120, 0, "", border="T")
