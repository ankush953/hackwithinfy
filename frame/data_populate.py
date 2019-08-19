import pandas as pd
from frame.models import FrameModel


# def populate():
#     df = pd.read_csv('../info.csv')
#     # print(df)
#     for i in range(df.shape[0]):
#         # normal_image = open("../%dNormal.jpg" % (i))
#         # depth_image = open("../%dDepth.jpg" % (i))
#         # processed_image = open("../%dProcessed.jpg" % (i))
#         normal_image = "../%dNormal.jpg" % i
#         mean = df['mean'][i]
#         median = df['median'][i]
#         variance = df['variance'][i]
#         standard_deviation = df['standard_deviation'][i]
#         image_type = df['image_type'][i].strip()
#         # print(mean,median,variance,standard_deviation,image_type)
#         obj = FrameModel(normal_image=normal_image, depth_image=depth_image, processed_image=processed_image,
#                          mean=mean, median=median, variance=variance, standard_deviation=standard_deviation, image_type=image_type)
#         obj.save()


def populate():
    file = open('../info.csv')
    # print(df)
    i = 0
    for line in file:
        # print(line)
        line = line.strip().split(',')
        if line[0] == 'mean':
            continue
        # normal_image = open("hackwithinfy_hackthon/%dNormal.jpg" % (i))
        # depth_image = open("../%dDepth.jpg" % (i))
        # processed_image = open("../%dProcessed.jpg" % (i))

        normal_image_loc = 'hackwithinfy_hackthon/%dNormal.jpg' % i
        depth_image_loc = 'hackwithinfy_hackthon/%dDepth.jpg' % i
        processed_image_loc = 'hackwithinfy_hackthon/%dProcessed.jpg' % i

        i += 1
        mean = float(line[0])
        median = float(line[1])
        variance = float(line[2])
        standard_deviation = float(line[3])
        image_type = line[4]
        # print(mean,median,variance,standard_deviation,image_type)
        obj = FrameModel(normal_image_loc=normal_image_loc, depth_image_loc=depth_image_loc, processed_image_loc=processed_image_loc,
                         mean=mean, median=median, variance=variance, standard_deviation=standard_deviation, image_type=image_type)
        obj.save()
        # normal_image = open("../%dNormal.jpg" % (i))
        # depth_image = open("../%dDepth.jpg" % (i))
        # processed_image = open("../%dProcessed.jpg" % (i))
        # mean = df['mean'][i]
        # median = df['median'][i]
        # variance = df['variance'][i]
        # standard_deviation = df['standard_deviation'][i]
        # image_type = df['image_type'][i].strip()
        # # print(mean,median,variance,standard_deviation,image_type)
        # obj = FrameModel(normal_image=normal_image, depth_image=depth_image, processed_image=processed_image,
        #                  mean=mean, median=median, variance=variance, standard_deviation=standard_deviation, image_type=image_type)
        # obj.save()
