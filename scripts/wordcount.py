"""
Calculates word count stats for the book.
"""

import argparse
import glob
import statistics

PAGE_LEN = 400


def main():
    parser = argparse.ArgumentParser(description='Calculate word count stats for the book')
    parser.add_argument('--page-len', type=int, default=PAGE_LEN,
                        help=f'Words per page (default: {PAGE_LEN})')
    args = parser.parse_args()

    filenames = sorted(glob.glob('chapters/[0-9][0-9]_*.md'))

    if not filenames:
        print('No chapter files found in chapters/ directory')
        return

    minmax = dict(
        shortest=(filenames[0], 1_000_000),
        longest=(filenames[0], 0),
    )

    print(f'Found {len(filenames)} chapters')
    word_counts = []
    
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as fp:
            content = fp.read()
            words = content.split()
            word_count = len(words)
            word_counts.append(word_count)
            
            # update minmax
            if word_count < minmax['shortest'][1]:
                minmax['shortest'] = (filename, word_count)
            if word_count > minmax['longest'][1]:
                minmax['longest'] = (filename, word_count)
            print(f'{filename}: {word_count} words')

    total_words = sum(word_counts)
    print(f'Total words in book: {total_words}')
    print(f'Total pages in book: {total_words // args.page_len + 1}')
    print(f'Average words per chapter: {total_words / len(filenames):.2f}')
    print(f'Shortest chapter: {minmax["shortest"][0]} ({minmax["shortest"][1]} words)')
    print(f'Longest chapter: {minmax["longest"][0]} ({minmax["longest"][1]} words)')
    
    if len(word_counts) > 1:
        std_dev = statistics.stdev(word_counts)
        print(f'Standard deviation of word count: {std_dev:.2f}')
    else:
        print('Standard deviation: N/A (need at least 2 chapters)')


if __name__ == '__main__':
    main()
