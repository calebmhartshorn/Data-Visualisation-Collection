import csv

filenames = ["five_chord_songs.csv", "four_chord_songs.csv"]

transitions = {}

domain = ['1', '2', '3', '4', '5', '6']
names = ['I', 'ii', 'iii', 'IV', 'V', 'vi']


for filename in filenames:
    with open(filename, newline='') as csvFile:
        csvReader = csv.reader(csvFile)
        for row in csvReader:
            chords = row[0].split(',')
            for i in range(len(chords)):

                fromChord = chords[i % len(chords)]
                toChord = chords[(i + 1) % len(chords)]

                if not (fromChord in domain and toChord in domain):
                    continue

                if fromChord == toChord:
                    continue

                key = fromChord + "->" + toChord
                if not key in transitions:
                    transitions[key] = 0

                transitions[key] += 1

for key in transitions:
    print(key.ljust(10, ' ') + str(transitions[key]))

with open('output.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    
    spamwriter.writerow(["", "", ""])

    for key in transitions:
        fromChord = key.split('->')[0]
        toChord = key.split('->')[1]
        spamwriter.writerow([names[int(fromChord) - 1], names[int(toChord) - 1], transitions[key]])
