import os
import cv2
import argparse
import numpy as np
import matplotlib.pyplot as plt

import __init_paths
from face_enhancement import FaceEnhancement


def display(img1, img2):
    fig = plt.figure(figsize=(25, 10))
    ax1 = fig.add_subplot(1, 2, 1)
    plt.title('Input image', fontsize=16)
    ax1.axis('off')
    ax2 = fig.add_subplot(1, 2, 2)
    plt.title('GPEN output', fontsize=16)
    ax2.axis('off')
    ax1.imshow(img1)
    ax2.imshow(img2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, default='GPEN-BFR-512', help='GPEN model')
    parser.add_argument('--task', type=str, default='FaceEnhancement', help='task of GPEN model')
    parser.add_argument('--key', type=str, default=None, help='key of GPEN model')
    parser.add_argument('--in_size', type=int, default=512, help='in resolution of GPEN')
    parser.add_argument('--out_size', type=int, default=None, help='out resolution of GPEN')
    parser.add_argument('--channel_multiplier', type=int, default=2, help='channel multiplier of GPEN')
    parser.add_argument('--narrow', type=float, default=1, help='channel narrow scale')
    parser.add_argument('--alpha', type=float, default=1, help='blending the results')
    parser.add_argument('--use_sr', action='store_true', help='use sr or not')
    parser.add_argument('--use_cuda', action='store_true', help='use cuda or not')
    parser.add_argument('--save_face', action='store_true', help='save face or not')
    parser.add_argument('--aligned', action='store_true', help='input are aligned faces or not')
    parser.add_argument('--sr_model', type=str, default='realesrnet', help='SR model')
    parser.add_argument('--sr_scale', type=int, default=2, help='SR scale')
    parser.add_argument('--tile_size', type=int, default=0, help='tile size for SR to avoid OOM')
    parser.add_argument('--indir', type=str, default='examples/imgs', help='input folder')
    parser.add_argument('--outdir', type=str, default='results/outs-bfr', help='output folder')
    parser.add_argument('--ext', type=str, default='.jpg', help='extension of output')
    args = parser.parse_args()

    # model = {'name':'GPEN-BFR-512', 'sr_model':'realesrnet', 'sr_scale': 2, 'size':512, 'channel_multiplier':2, 'narrow':1}
    # model = {'name':'GPEN-BFR-256', 'sr_model':'realesrnet', 'size':256, 'channel_multiplier':1, 'narrow':0.5}

    os.makedirs(args.outdir, exist_ok=True)

    faceenhancer = FaceEnhancement(args, in_size=args.in_size, model=args.model, use_sr=args.use_sr,
                                   device='cuda' if args.use_cuda else 'cpu')
    # МЕСТО ДЛЯ ВЫБОРА ФОТО
    for filename in os.listdir(os.path.join(args.indir)):
        file = os.path.join(args.indir, filename)
        print("processing " + filename)
        img = cv2.imread(file, cv2.IMREAD_COLOR)  # BGR
        # im = cv2.resize(im, (0,0), fx=2, fy=2) #optional

        img_out, orig_faces, enhanced_faces = faceenhancer.process(img, aligned=False)

        img = cv2.resize(img, img_out.shape[:2][::-1])
        cv2.imwrite(os.path.join(args.outdir, '.'.join(filename.split('.')[:-1]) + '_COMP.jpg'), np.hstack((img, img_out)))
        cv2.imwrite(os.path.join(args.outdir, '.'.join(filename.split('.')[:-1]) + '_GPEN.jpg'), img_out)

        for m, (ef, of) in enumerate(zip(enhanced_faces, orig_faces)):
            of = cv2.resize(of, ef.shape[:2])
            cv2.imwrite(os.path.join(args.outdir, '.'.join(filename.split('.')[:-1]) + '_face%02d' % m + '.jpg'),
                        np.hstack((of, ef)))

        display(img, img_out)