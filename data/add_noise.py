'''
Add noise to pngs in a folder;
Bave to another folder;
Write a list of "<clean> <noisy>\n" pngs in a file

After this can run:

    th scripts/im_pairs_to_torch.lua data/imglist.txt 5000 data/thimgs 4000

From the main SPEN path. This will create 2 files, one with 4000 and the other
with 1000 imgs pairs for train and test.
'''

import numpy
import os
import scipy.misc


def add_noise(clean, noisy):
    '''
    Open a PNG file in path `clean`, add Gaussian noise to it,
    then write resulting PNG to file path `noisy`
    '''
    imagea = (scipy.misc.imread(clean)).astype(float)
    gaussNoise = numpy.random.normal(0, 10,imagea.shape).astype(float)
    imageb = imagea + gaussNoise
    scipy.misc.imsave(noisy, imageb)


if __name__ == '__main__':
    cleandir = 'clean/'  # file containing clean PNG to add noise to
    noisydir = 'noisy/'  # file to write noisy PNG's to
    filelist= 'imglist.txt' # text file to write clean/noisy pairs to

    png_list_file = open(filelist, 'w')

    for (dirpath, dirnames, filenames) in os.walk(cleandir):
        for imgfile in filenames:
            if imgfile.endswith('.png'):
                clean_name = os.path.join('data/', cleandir, imgfile)
                noisy_name = os.path.join('data/', noisydir, imgfile)
                add_noise(clean_name, noisy_name)
                png_list_file.write('%s %s\n' % (clean_name, noisy_name))

    png_list_file.close()


