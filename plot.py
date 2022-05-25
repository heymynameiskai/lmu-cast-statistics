import matplotlib.pyplot as plt
import numpy as np


# labels = ['G1', 'G2', 'Gnfkdlsnfjakdnkl3', 'G4', 'G5']
# online = np.array((100, 35, 30, 35, 27))
# video = np.array((30, 35, 30, 35, 27))
# audio = np.array((5, 35, 30, 35, 27))
#
# width = 0.5       # the width of the bars: can also be len(x) sequence
# 
# fig, ax = plt.subplots()
#
# ax.bar(labels, online, width, label='Online', color='#0099ff')
# ax.bar(labels, video, width, bottom=online, label='Video', color='#33cc33')
# ax.bar(labels, audio, width, bottom=online+video, label='Audio', color='#ff9900')
#
# plt.xticks(rotation=90)
#
#
# ax.set_ylabel('Aufrufe')
# ax.set_title('Aufrufe nach Video und Format')
# ax.legend()
#
# plt.savefig('plot.pdf', format='pdf')


def plot(playlist_id, statistics):
    # labels = []
    labels = []
    online = []
    video = []
    audio = []
    online_video_sum = []


    for k in sorted(statistics.keys()):
        # reorder hits for mathplot
        labels.append(statistics[k]['title'])
        online.append(int(statistics[k]['hits_online']))
        video.append(int(statistics[k]['hits_video']))
        audio.append(int(statistics[k]['hits_audio']))
        online_video_sum.append(int(statistics[k]['hits_online']) + int(statistics[k]['hits_video']))





    
    # plot
    fig, ax = plt.subplots()

    ax.bar(labels, online, label='Online', color='#0099ff')
    ax.bar(labels, video, bottom=online, label='Video', color='#33cc33')
    ax.bar(labels, audio, bottom=online_video_sum, label='Audio', color='#ff9900')

    ax.set_ylabel('Aufrufe')
    ax.set_title('Aufrufe nach Video und Format')
    ax.legend()

    plt.subplots_adjust(bottom=0.5)
    plt.xticks(rotation=90)
    plt.savefig('export_pdf/tmp/'+playlist_id+'.png', format='png', dpi=300)
