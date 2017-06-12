#!/usr/bin/env python
# -*- coding, utf-8 -*-
"""
.py
~~~

PURPOSE


REFERENCES


REQUIRES


,author: R.K.Garcia <rayg@ssec.wisc.edu>
,copyright: 2014 by University of Wisconsin Regents, see AUTHORS for more details
,license: GPLv3, see LICENSE for more details
"""
__docformat__ = 'reStructuredText'
__author__ = 'cphillips'

from vispy.color.colormap import Colormap, BaseColormap, _mix_simple, _colormaps
from collections import OrderedDict
import numpy as np


def _get_awips_colors(cmap_file):
    from xml.etree import ElementTree
    tree = ElementTree.parse(cmap_file)
    colors = np.array([(float(c.get('r')), float(c.get('g')), float(c.get('b'))) for c in tree.findall('color')])
    return colors


def generate_from_awips_cmap(cmap_file):

    colors = _get_awips_colors(cmap_file)

    skp = 0
    control_indexes = [0]
    bp = np.round(colors[0] * 255.)
    lp = np.round(colors[1] * 255.)
    bpd = 1
    cn = 2
    for c in colors[2:-1]:
     ep = 1.0 / bpd
     cc = np.round(c * 255.)
     rcs = cc[0] - lp[0]
     gcs = cc[1] - lp[1]
     bcs = cc[2] - lp[2]
     rds = (lp[0] - bp[0]) / bpd
     gds = (lp[1] - bp[1]) / bpd
     bds = (lp[2] - bp[2]) / bpd
     cd = np.round(colors[cn+1] * 255.)
     res = 0.5 * (cd[0] - lp[0])
     ges = 0.5 * (cd[1] - lp[1])
     bes = 0.5 * (cd[2] - lp[2])
     if skp == 1:
      bpd += 1
      skp = 0
     elif (rcs*rds >= 0 and gcs*gds >= 0 and bcs*bds >= 0) and \
      ((abs(rcs) > np.ceil(abs(rds)+ep) and abs(res) < abs(rcs)) or (abs(rcs) < np.floor(abs(rds)-ep) and abs(res) > abs(rcs)) or \
       np.floor(abs(rds)-ep) <= abs(rcs) <= np.ceil(abs(rds)+ep)) and \
      ((abs(gcs) > np.ceil(abs(gds)+ep) and abs(ges) < abs(gcs)) or (abs(gcs) < np.floor(abs(gds)-ep) and abs(ges) > abs(gcs)) or \
       np.floor(abs(gds)-ep) <= abs(gcs) <= np.ceil(abs(gds)+ep)) and \
      ((abs(bcs) > np.ceil(abs(bds)+ep) and abs(bes) < abs(bcs)) or (abs(bcs) < np.floor(abs(bds)-ep) and abs(bes) > abs(bcs)) or \
       np.floor(abs(bds)-ep) <= abs(bcs) <= np.ceil(abs(bds)+ep)):
      bpd += 1
     else:
      control_indexes.append(cn-1)
      bp = lp
      bpd = 1
      skp = 1
     lp = cc
     cn += 1
    control_indexes.append(cn)

#    changes = np.abs(np.diff(np.diff(colors, axis=0), axis=0))
#    second_order_indexes = np.sort(list({0, colors.shape[0] - 1} |
#                              set(np.nonzero(changes[:, 0] > np.mean(changes[np.nonzero(changes[:, 0]), 0]))[0] + 1) |
#                              set(np.nonzero(changes[:, 1] > np.mean(changes[np.nonzero(changes[:, 1]), 1]))[0] + 1) |
#                              set(np.nonzero(changes[:, 2] > np.mean(changes[np.nonzero(changes[:, 2]), 2]))[0] + 1)
#                                                                           ))

    control_points = np.array(control_indexes) / cn
    hex_colors = ["#{:02x}{:02x}{:02x}".format(*[int(x*255) for x in c])
                  for c in colors[control_indexes]]

#    red_changes = np.nonzero(np.abs(np.diff(np.diff(colors[:, 0]))) > 1e-7)[0] + 1
#    green_changes = np.nonzero(np.abs(np.diff(np.diff(colors[:, 1]))) > 1e-7)[0] + 1
#    blue_changes = np.nonzero(np.abs(np.diff(np.diff(colors[:, 2]))) > 1e-7)[0] + 1
#    control_indexes = sorted({0} | {colors.shape[0] - 1} | set(red_changes) | set(green_changes) | set(blue_changes))
    return control_points, hex_colors


def generate_awips_cmap_debug_plot(cmap_file, out_fn):
    import matplotlib.pyplot as plt
    colors = _get_awips_colors(cmap_file)
    velocity = np.diff(colors, axis=0)
    acc = np.abs(np.diff(velocity, axis=0))
    fig = plt.figure()
    # 3 columns - R, G, B
    # 3 Rows - color, vel, acc
    ax = fig.add_subplot(3, 3, 1)
    ax.set_ylabel('Color')
    ax.set_title('Red')
    ax.plot(colors[:, 0])
    ax = fig.add_subplot(3, 3, 2)
    ax.set_title('Green')
    ax.plot(colors[:, 0])
    ax = fig.add_subplot(3, 3, 3)
    ax.set_title('Blue')
    ax.plot(colors[:, 2])

    ax = fig.add_subplot(3, 3, 4)
    ax.set_ylabel('Velocity')
    ax.plot(velocity[:, 0])
    ax = fig.add_subplot(3, 3, 5)
    ax.plot(velocity[:, 1])
    ax = fig.add_subplot(3, 3, 6)
    ax.plot(velocity[:, 2])

    ax = fig.add_subplot(3, 3, 7)
    ax.set_ylabel('Acceleration')
    ax.plot(acc[:, 0])
    ax = fig.add_subplot(3, 3, 8)
    ax.plot(acc[:, 1])
    ax = fig.add_subplot(3, 3, 9)
    ax.plot(acc[:, 2])

    plt.savefig(out_fn)


class SquareRootColormap(BaseColormap):
    colors = [(0.0, 0.0, 0.0, 1.0),
              (1.0, 1.0, 1.0, 1.0)]

    glsl_map = """
    vec4 sqrt_cmap(float t) {
        return mix($color_0, $color_1, sqrt(t));
    }
    """

    def map(self, t):
        a, b = self.colors.rgba
        return _mix_simple(a, b, np.sqrt(t))


class FlippedColormap(Colormap):
    """Simple wrapper to flip the provide colors and colormaps.
    """
    def __init__(self, colors, controls, **kwargs):
        colors = colors[::-1]
        controls = [1-x for x in controls][::-1]
        super().__init__(colors, controls=controls, **kwargs)


# Hand made colormap for the CIRA IR Default colormap
# The XML file from AWIPS doesn't separate things very well or in a way that can be easily automated
# we have to include every break point
cira_ir_colors = [(0.0, 0.0, 0.0, 1.0), # Black
          (0.980392156862745, 0.980392156862745, 0.980392156862745, 1.0), # White
          (0.972549019607843, 0.949019607843137, 0, 1.0), # Bright Yellow
          (0.372549019607843, 0.372549019607843, 0.0, 1.0), # Dark Yellow
          (0.564705882352941, 0.0, 0.0, 1.0), # Dark Red
          (0.929411764705882, 0.0, 0.0, 1.0), # Bright Red
          (0.949019607843137, 0.0, 0.972549019607843, 1.0), # Bright magenta
          (0.549019607843137, 0.0, 0.552941176470588, 1.0), # Dark magenta
          (0.0, 0.372549019607843, 0.564705882352941, 1.0), # Dark Cyan
          (0.0, 0.780392156862745, 0.815686274509804, 1.0), # Bright Cyan
          (0.0470588235294118, 0.972549019607843, 0.0, 1.0), # Bright Green
          (0.0, 0.435294117647059, 0.0, 1.0), # Dark Green
          (0.0235294117647059, 0.0, 0.0, 1.0), # Black
          (0.847058823529412, 0.847058823529412, 0.847058823529412, 1.0), # white-ish
          (0.00392156862745098, 0.0, 0.972549019607843, 1.0), # Bright Blue
          (0.0, 0.0, 0.4, 1.0), # Dark Blue
          (0.972549019607843, 0.0, 0.466666666666667, 1.0), # Bright Red
          (0.0980392156862745, 0.0, 0.0392156862745098, 1.0), # Dark Red
          (1.0, 1.0, 1.0, 1.0),
          (1.0, 1.0, 1.0, 1.0),
          ]

cira_ir_segment_indexes = [
    55,
    -30,
    -40,
    -50,
    -60,
    -70,
    -80,
    -90,
    -100,
    -108,
    -109,
]
cira_ir_controls = [(y - 55)/(-109 - 55) for x in cira_ir_segment_indexes for y in [x, x]][1:-1]

cira_ir_default = FlippedColormap(cira_ir_colors, controls=cira_ir_controls)



# Modified cloud_amount_default with 1.0 bounds value
_cloud_amount_default_control_points = (0.0, 0.03137254901960784, 0.2196078431372549, 0.23137254901960785, 0.2627450980392157, 0.29411764705882354, 0.2980392156862745, 0.996078431372549, 1.0)
_cloud_amount_default_colors = ('#000000', '#181818', '#bababa', '#c4c4c4', '#e0e0e0', '#fbfbfb', '#ffa67d', '#ffff00', '#ffff00')
cloud_amount_default = Colormap(colors=_cloud_amount_default_colors, controls=_cloud_amount_default_control_points)
_cloud_top_height_control_points = (0.0, 0.2901960784313726, 0.4549019607843137, 0.611764705882353, 0.7843137254901961, 0.8, 0.8156862745098039, 0.8235294117647058, 0.8627450980392157, 0.9019607843137255, 1.0)
_cloud_top_height_colors = ('#000000', '#020202', '#ac7070', '#a18331', '#41a166', '#211d8a', '#211d89', '#05f7fb', '#fbf702', '#fb0000', '#ffffff')
cloud_top_height = Colormap(colors=_cloud_top_height_colors, controls=_cloud_top_height_control_points)
# Modified low_cloud_base with 1.0 bounds value
_low_cloud_base_control_points = (0.0, 0.11764705882352941, 0.12549019607843137, 0.1450980392156863, 0.21176470588235294, 0.30196078431372547, 0.3058823529411765, 0.4980392156862745, 0.5450980392156862, 0.5490196078431373, 0.7843137254901961, 1.0)
_low_cloud_base_colors = ('#00aac7', '#008cab', '#ffffff', '#0087a6', '#007597', '#005a82', '#005981', '#7f7f7f', '#8a8a8a', '#8b8b8b', '#ff0000', '#ff0000')
low_cloud_base = Colormap(colors=_low_cloud_base_colors, controls=_low_cloud_base_control_points)
_rain_rate_control_points = (0.0, 0.5215686274509804, 0.6, 0.6470588235294118, 0.6980392156862745, 0.7490196078431373, 0.8, 0.8392156862745098, 0.8431372549019608, 0.8941176470588236, 1.0)
_rain_rate_colors = ('#000000', '#c7c7c7', '#00ffff', '#0000ff', '#00ff00', '#ffff00', '#ff9500', '#e20000', '#f00000', '#ff00ff', '#ffffff')
rain_rate = Colormap(colors=_rain_rate_colors, controls=_rain_rate_control_points)

_color11new_control_points = (0.0, 0.0024425989252564728,
 0.064484611626770882, 0.12701514411333659, 0.189057156814851,
 0.25158768930141673, 0.31411822178798243, 0.37616023448949681,
 0.43869076697606252, 0.50122129946262828, 0.56375183194919398,
 0.62579384465070831, 0.68832437713727401, 0.75085490962383972,
 0.87542745481191986, 1.0)
_color11new_colors = ['#7e0000', '#000000', '#7e3e1f', '#ff0000', '#ff7e7e',
 '#ffff00', '#7eff7e', '#00ff00', '#007e7e', '#00ffff', '#7e7eff', '#0000ff',
 '#7e007e', '#ff00ff', '#ffffff', '#000000']
color11new = FlippedColormap(colors=_color11new_colors, controls=_color11new_control_points)
# _cira_ir_default_control_points = (0.0, 0.6627450980392157, 0.7215686274509804, 0.7254901960784313, 0.7607843137254902, 0.8, 0.803921568627451, 0.8470588235294118, 0.8901960784313725, 0.9215686274509803, 0.9568627450980393, 0.9921568627450981, 1.0)
# _cira_ir_default_colors = ('#000000', '#f9f9f9', '#686600', '#5e5a00', '#e20000', '#97009b', '#8b008c', '#00c6d0', '#006f00', '#d8d8d8', '#000077', '#360017', '#ffffff')
# cira_ir_default = Colormap(colors=_cira_ir_default_colors, controls=_cira_ir_default_control_points)
_fog_control_points = (0.0, 0.027450980392156862, 0.17647058823529413, 0.24313725490196078, 0.3254901960784314, 0.3764705882352941, 1.0)
_fog_colors = ('#000000', '#0c0c0c', '#4e4e4e', '#6d6d6d', '#919191', '#a9a9a9', '#ffffff')
fog = Colormap(colors=_fog_colors, controls=_fog_control_points)
_ir_wv_control_points = (0.0, 0.6431372549019608, 0.7607843137254902, 0.8, 0.803921568627451, 0.8470588235294118, 0.8901960784313725, 0.9215686274509803, 0.9568627450980393, 0.9921568627450981, 1.0)
_ir_wv_colors = ('#000000', '#f5f5f5', '#df0000', '#94009a', '#8a008a', '#00c4ce', '#006d00', '#d5d5d5', '#000076', '#350016', '#ffffff')
ir_wv = FlippedColormap(colors=_ir_wv_colors, controls=_ir_wv_control_points)
_lifted_index__new_cimss_table_control_points = (0.0, 0.4823529411764706, 0.5607843137254902, 0.5647058823529412, 0.6392156862745098, 0.6431372549019608, 0.7176470588235294, 0.7215686274509804, 0.7843137254901961, 0.9921568627450981, 1.0)
_lifted_index__new_cimss_table_colors = ('#000000', '#412a0e', '#7876cf', '#7b79d4', '#767502', '#706f02', '#ea0000', '#f10000', '#f575c7', '#c6c6c5', '#ffffff')
lifted_index__new_cimss_table = Colormap(colors=_lifted_index__new_cimss_table_colors, controls=_lifted_index__new_cimss_table_control_points)
_lifted_index_default_control_points = (0.0, 0.20392156862745098, 0.2901960784313726, 0.29411764705882354, 0.34901960784313724, 0.35294117647058826, 0.40784313725490196, 0.4627450980392157, 0.4666666666666667, 0.5215686274509804, 0.6392156862745098, 0.6431372549019608, 0.6941176470588235, 0.7803921568627451, 1.0)
_lifted_index_default_colors = ('#000000', '#7f1818', '#0abf06', '#07c405', '#7382c3', '#7b8cc6', '#ca9444', '#bac005', '#bec403', '#ca84c0', '#c37801', '#c67b01', '#b200b6', '#c27ec4', '#ffffff')
lifted_index_default = Colormap(colors=_lifted_index_default_colors, controls=_lifted_index_default_control_points)
# Modified blended_total_precip_water with 1.0 bounds value
_blended_total_precip_water_control_points = (0.0, 0.011764705882352941, 0.7372549019607844, 0.7764705882352941, 0.7843137254901961, 0.8313725490196079, 0.8352941176470589, 0.8588235294117647, 0.8823529411764706, 0.9294117647058824, 0.9333333333333333, 0.9803921568627451, 0.9882352941176471, 1.0)
_blended_total_precip_water_colors = ('#000000', '#db9270', '#0000c4', '#00e7e7', '#00ffff', '#00f300', '#00ff00', '#b9b900', '#ffff00', '#f30000', '#ff0000', '#f300f3', '#ffffff', '#ffffff')
blended_total_precip_water = Colormap(colors=_blended_total_precip_water_colors, controls=_blended_total_precip_water_control_points)
# Modified percent_of_normal_tpw with 1.0 bounds value
_percent_of_normal_tpw_control_points = (0.0, 0.12156862745098039, 0.13333333333333333, 0.17254901960784313, 0.29411764705882354, 0.5843137254901961, 0.6431372549019608, 0.7019607843137254, 0.7098039215686275, 0.7450980392156863, 0.7764705882352941, 0.7803921568627451, 0.984313725490196, 1.0)
_percent_of_normal_tpw_colors = ('#000000', '#875a45', '#94634c', '#c08062', '#ecc9b7', '#05ffff', '#00dbdb', '#00b4b4', '#00b0b0', '#009999', '#008484', '#008181', '#ffffff', '#ffffff')
percent_of_normal_tpw = Colormap(colors=_percent_of_normal_tpw_colors, controls=_percent_of_normal_tpw_control_points)
_precip_water__new_cimss_table_control_points = (0.0, 0.10980392156862745, 0.23137254901960785, 0.34901960784313724, 0.4627450980392157, 0.5764705882352941, 0.5803921568627451, 0.6941176470588235, 0.788235294117647, 0.9921568627450981, 1.0)
_precip_water__new_cimss_table_colors = ('#000000', '#4c3516', '#9390f2', '#0a675e', '#9fc33c', '#f3775c', '#f77a5e', '#700071', '#ffc2fc', '#c6c6c6', '#ffffff')
precip_water__new_cimss_table = Colormap(colors=_precip_water__new_cimss_table_colors, controls=_precip_water__new_cimss_table_control_points)
_precip_water__polar_control_points = (0.0, 0.6862745098039216, 0.7333333333333333, 0.7372549019607844, 0.796078431372549, 0.8156862745098039, 0.8509803921568627, 0.8745098039215686, 0.9294117647058824, 1.0)
_precip_water__polar_colors = ('#000000', '#ffffff', '#f1f100', '#ffff00', '#00bbef', '#00ffff', '#aa0000', '#ff0000', '#c7ffc7', '#ffffff')
precip_water__polar = Colormap(colors=_precip_water__polar_colors, controls=_precip_water__polar_control_points)
_precip_water_default_control_points = (0.0, 0.09411764705882353, 0.21176470588235294, 0.25098039215686274, 0.2901960784313726, 0.32941176470588235, 0.3686274509803922, 0.40784313725490196, 0.4823529411764706, 0.48627450980392156, 0.49411764705882355, 0.4980392156862745, 0.7803921568627451, 1.0)
_precip_water_default_colors = ('#000000', '#850200', '#ca2b00', '#ca9117', '#6bac1f', '#22ac4a', '#279fa1', '#821ba1', '#2629a6', '#1e1fa1', '#ca4205', '#ca8203', '#070355', '#ffffff')
precip_water_default = Colormap(colors=_precip_water_default_colors, controls=_precip_water_default_control_points)
_skin_temp__new_cimss_table_control_points = (0.0, 0.17254901960784313, 0.17647058823529413, 0.25098039215686274, 0.2549019607843137, 0.3333333333333333, 0.40784313725490196, 0.48627450980392156, 0.49019607843137253, 0.6431372549019608, 0.7764705882352941, 0.7803921568627451, 1.0)
_skin_temp__new_cimss_table_colors = ('#000000', '#cc5111', '#cc5211', '#f6e207', '#faeb07', '#1aaf03', '#03edd9', '#0523ff', '#0517ff', '#fcedff', '#1afcff', '#13fcff', '#ffffff')
skin_temp__new_cimss_table = Colormap(colors=_skin_temp__new_cimss_table_colors, controls=_skin_temp__new_cimss_table_control_points)
_skin_temp_default_control_points = (0.0, 0.2901960784313726, 0.2980392156862745, 0.3764705882352941, 0.5333333333333333, 0.6901960784313725, 0.8, 0.8156862745098039, 0.8235294117647058, 0.8627450980392157, 0.9019607843137255, 1.0)
_skin_temp_default_colors = ('#000000', '#020202', '#9d3c5e', '#9d4c00', '#9d9900', '#1a8c63', '#211d8b', '#211d8a', '#05f8fc', '#fcf802', '#fc0000', '#ffffff')
skin_temp_default = Colormap(colors=_skin_temp_default_colors, controls=_skin_temp_default_control_points)
_ca_low_light_vis_control_points = (0.0, 0.3333333333333333, 0.6901960784313725, 0.7333333333333333, 0.7764705882352941, 1.0)
_ca_low_light_vis_colors = ('#000000', '#818181', '#ffffff', '#9b9b9b', '#464646', '#777777')
ca_low_light_vis = Colormap(colors=_ca_low_light_vis_colors, controls=_ca_low_light_vis_control_points)
_linear_control_points = (0.0, 0.2980392156862745, 0.4980392156862745, 0.6980392156862745, 0.7058823529411765, 0.8862745098039215, 1.0)
_linear_colors = ('#000000', '#4c4c4c', '#7f7f7f', '#b1b1b1', '#b4b4b4', '#e2e2e2', '#ffffff')
linear = Colormap(colors=_linear_colors, controls=_linear_control_points)
# Modified za_vis_default with 1.0 bounds value
_za_vis_default_control_points = (0.0, 0.23921568627450981, 0.2627450980392157, 0.34901960784313724, 0.5176470588235295, 0.8627450980392157, 1.0)
_za_vis_default_colors = ('#000000', '#0b0b0b', '#181818', '#4c4c4c', '#848484', '#ffffff', '#ffffff')
za_vis_default = Colormap(colors=_za_vis_default_colors, controls=_za_vis_default_control_points)
_gray_scale_water_vapor_control_points = (0.0, 0.6274509803921569, 0.7176470588235294, 0.7803921568627451, 0.9803921568627451, 0.9921568627450981, 1.0)
_gray_scale_water_vapor_colors = ('#000000', '#2e2e2e', '#606060', '#838383', '#f0f0f0', '#f6f6f6', '#ffffff')
gray_scale_water_vapor = FlippedColormap(colors=_gray_scale_water_vapor_colors, controls=_gray_scale_water_vapor_control_points)
_nssl_vas_wv_alternate_control_points = (0.0, 0.42745098039215684, 0.47058823529411764, 0.5490196078431373, 0.6274509803921569, 0.6588235294117647, 0.6745098039215687, 0.6901960784313725, 0.7058823529411765, 0.7843137254901961, 0.9098039215686274, 1.0)
_nssl_vas_wv_alternate_colors = ('#000000', '#9e0000', '#7f0000', '#9e3f00', '#9e7f00', '#529e00', '#2bad00', '#00be45', '#009e6a', '#006a9e', '#a6a6a6', '#ffffff')
nssl_vas_wv_alternate = FlippedColormap(colors=_nssl_vas_wv_alternate_colors, controls=_nssl_vas_wv_alternate_control_points)
_ramsdis_wv_control_points = (0.0, 0.7450980392156863, 0.8, 0.8392156862745098, 0.8745098039215686, 0.9019607843137255, 0.9098039215686274, 0.9137254901960784, 0.9568627450980393, 1.0)
_ramsdis_wv_colors = ('#000000', '#e5e5e5', '#0200ee', '#02ee02', '#df0000', '#ac4801', '#ffffff', '#626148', '#606060', '#ffffff')
ramsdis_wv = FlippedColormap(colors=_ramsdis_wv_colors, controls=_ramsdis_wv_control_points)
_slc_wv_control_points = (0.0, 0.5529411764705883, 0.6431372549019608, 0.7686274509803922, 0.8196078431372549, 0.8235294117647058, 0.8274509803921568, 0.8627450980392157, 0.8862745098039215, 0.8901960784313725, 0.9137254901960784, 0.9254901960784314, 1.0)
_slc_wv_colors = ('#000000', '#995c35', '#3a3835', '#759285', '#166f4c', '#076a44', '#036842', '#008484', '#00b0b0', '#00b6b6', '#009300', '#006c00', '#ffffff')
slc_wv = FlippedColormap(colors=_slc_wv_colors, controls=_slc_wv_control_points)

# TOWRS
_actp_control_points = (0.0, 0.16666666666666666, 0.6666666666666666, 1.0)
_actp_colors = ('#000000', '#00ffff', '#ff0000', '#000000')
actp = Colormap(colors=_actp_colors, controls=_actp_control_points)
_adp_control_points = (0.0, 0.375, 0.625, 1.0)
_adp_colors = ('#000000', '#0000ff', '#ff0000', '#000000')
adp = Colormap(colors=_adp_colors, controls=_adp_control_points)
_rrqpe_control_points = (0.0, 0.001669449081803005, 0.1652754590984975, 0.1686143572621035, 0.332220367278798, 0.335559265442404, 0.4991652754590985, 0.5025041736227045, 0.666110183639399, 0.669449081803005, 0.8330550918196995, 0.8363939899833055, 1.0)
_rrqpe_colors = ('#000000', '#fd7efd', '#9a1a9a', '#7ecafd', '#1a679a', '#7efd7e', '#1a9a1a', '#fdfd7e', '#9a9a1a', '#fdca7e', '#9a671a', '#fd7e7e', '#9a1a1a')
rrqpe = Colormap(colors=_rrqpe_colors, controls=_rrqpe_control_points)
_vtrsb_control_points = (0.0, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0)
_vtrsb_colors = ('#000000', '#7f00ff', '#0000ff', '#00ffff', '#00ff00', '#ffff00', '#ff0000')
vtrsb = Colormap(colors=_vtrsb_colors, controls=_vtrsb_control_points)
_colorhcapeh10_control_points = (0.0, 0.1270772238514174, 0.25024437927663734, 0.3421309872922776, 0.4975562072336266, 0.6119257086999023, 0.7302052785923754, 0.8719452590420332, 1.0)
_colorhcapeh10_colors = ('#4d3719', '#d7aa75', '#b3b3ff', '#5a5a99', '#ffff00', '#ff8270', '#ff0000', '#630066', '#ef00f4')
colorhcapeh10 = Colormap(colors=_colorhcapeh10_colors, controls=_colorhcapeh10_control_points)
_colorhlih10_control_points = (0.0, 0.09872922776148582, 0.17595307917888564, 0.2785923753665689, 0.4525904203323558, 0.5434995112414467, 0.6920821114369502, 0.804496578690127, 0.8807429130009775, 1.0)
_colorhlih10_colors = ('#f80000', '#770000', '#636d00', '#e8ff00', '#7f8bfd', '#3e4478', '#ffbb8f', '#747c7b', '#3b2b0b', '#d7b482')
colorhlih10 = Colormap(colors=_colorhlih10_colors, controls=_colorhlih10_control_points)
_colorhpw10h10_control_points = (0.0, 0.11632453567937438, 0.21407624633431085, 0.2883675464320626, 0.34701857282502446, 0.43206256109481916, 0.4555229716520039, 0.5356793743890518, 0.6275659824046921, 0.7047898338220919, 0.7497556207233627, 0.852394916911046, 1.0)
_colorhpw10h10_colors = ('#3b2709', '#d9a675', '#9696fa', '#4f4f96', '#006363', '#73a427', '#92bf3a', '#ffff00', '#ff8263', '#962727', '#630063', '#ef00ef', '#fec7fe')
colorhpw10h10 = Colormap(colors=_colorhpw10h10_colors, controls=_colorhpw10h10_control_points)
_colorhpw8h10_control_points = (0.0, 0.093841642228739, 0.176930596285435, 0.23949169110459434, 0.2883675464320626, 0.3597262952101662, 0.3782991202346041, 0.4467253176930596, 0.5249266862170088, 0.5904203323558163, 0.6275659824046921, 0.7145650048875856, 0.8387096774193549, 0.8582600195503421, 0.9345063538611925, 1.0)
_colorhpw8h10_colors = ('#422c0d', '#d9a675', '#9595f8', '#4f5095', '#006363', '#73a427', '#90be3b', '#ffff00', '#ff8263', '#952728', '#630063', '#ef00ef', '#ffc7ff', '#e1b3df', '#fe8265', '#962727')
colorhpw8h10 = Colormap(colors=_colorhpw8h10_colors, controls=_colorhpw8h10_control_points)
_ir_color_clouds_summer_control_points = (0.0, 0.48168050806057644, 0.48265754763067903, 0.5490962383976551, 0.646800195407914, 0.6951636541279922, 0.7625793844650708, 0.8236443575964827, 0.8847093307278945, 0.9574987787005373, 0.9960918417195896, 0.9970688812896922, 1.0)
_ir_color_clouds_summer_colors = ('#000000', '#c1c1c1', '#00fcfd', '#000073', '#00ff00', '#ffff00', '#ff0000', '#000000', '#e6e6e6', '#7f007f', '#13daec', '#06ced4', '#000000')
ir_color_clouds_summer = Colormap(colors=_ir_color_clouds_summer_colors, controls=_ir_color_clouds_summer_control_points)
_ir_color_clouds_winter_control_points = (0.0, 0.48216902784562776, 0.48314606741573035, 0.5490962383976551, 0.646800195407914, 0.6951636541279922, 0.7625793844650708, 0.8236443575964827, 0.8847093307278945, 0.9574987787005373, 0.9960918417195896, 0.9970688812896922, 1.0)
_ir_color_clouds_winter_colors = ('#000000', '#c1c1c1', '#00fafc', '#000073', '#00ff00', '#ffff00', '#ff0000', '#000000', '#e6e6e6', '#7f007f', '#13daec', '#06ced4', '#000000')
ir_color_clouds_winter = Colormap(colors=_ir_color_clouds_winter_colors, controls=_ir_color_clouds_winter_control_points)
_wv_dry_yellow_control_points = (0.0, 0.21299462628236443, 0.3048363458720078, 0.4211040547142159, 0.48216902784562776, 0.6101612115290669, 0.701514411333659, 1.0)
_wv_dry_yellow_colors = ('#000000', '#6c6c6c', '#ff0000', '#ffff00', '#000073', '#ffffff', '#438323', '#000000')
wv_dry_yellow = Colormap(colors=_wv_dry_yellow_colors, controls=_wv_dry_yellow_control_points)
_dust_and_moisture_split_window_control_points = (0.0, 0.0014655593551538837, 0.002442598925256473, 0.46555935515388375, 0.46653639472398634, 0.5002442598925256, 0.5339521250610649, 0.6170004885197851, 0.767953102100635, 0.8334147532975086, 1.0)
_dust_and_moisture_split_window_colors = ('#000000', '#5f5f5f', '#824513', '#fddcb1', '#ffdeae', '#ffffff', '#0000ff', '#ffff00', '#ff0000', '#ff00ff', '#ff00ff')
dust_and_moisture_split_window = Colormap(colors=_dust_and_moisture_split_window_colors, controls=_dust_and_moisture_split_window_control_points)
_enhancedhrainbowh11_control_points = (0.0, 0.002442598925256473, 0.06497313141182218, 0.1270151441133366, 0.31411822178798243, 0.37664875427454814, 0.5012212994626283, 0.688324377137274, 0.8754274548119199, 1.0)
_enhancedhrainbowh11_colors = ('#7e0000', '#000000', '#803e1e', '#ff0000', '#7eff00', '#007e00', '#00ffff', '#7e007e', '#ffffff', '#000000')
enhancedhrainbowh11 = Colormap(colors=_enhancedhrainbowh11_colors, controls=_enhancedhrainbowh11_control_points)
_enhancedhrainbow_warmer_yellow_control_points = (0.0, 0.30685675492192804, 0.35030549898167007, 0.39341479972844534, 0.5234215885947047, 0.5668703326544468, 0.653428377460964, 0.7834351663272233, 0.9134419551934827, 1.0)
_enhancedhrainbow_warmer_yellow_colors = ('#ffff00', '#000000', '#803e1f', '#ff0000', '#7fff00', '#007f00', '#00ffff', '#7f007f', '#ffffff', '#000000')
enhancedhrainbow_warmer_yellow = Colormap(colors=_enhancedhrainbow_warmer_yellow_colors, controls=_enhancedhrainbow_warmer_yellow_control_points)
_fire_detection_3p9_control_points = (0.0, 0.36590131900341966, 0.36687835857352225, 1.0)
_fire_detection_3p9_colors = ('#ff0000', '#fffc00', '#141414', '#ffffff')
fire_detection_3p9 = Colormap(colors=_fire_detection_3p9_colors, controls=_fire_detection_3p9_control_points)
_ramsdis_ir_12bit_control_points = (0.0, 0.505982905982906, 0.5064713064713064, 0.5794871794871795, 0.5851037851037851, 0.5855921855921856, 0.6466422466422467, 0.702075702075702, 0.7074481074481075, 0.7711843711843712, 0.7746031746031746, 0.8412698412698413, 0.8417582417582418, 0.8844932844932845, 0.8901098901098901, 0.8905982905982905, 0.9455433455433455, 0.9516483516483516, 1.0)
_ramsdis_ir_12bit_colors = ('#080808', '#ffffff', '#fdfd00', '#646400', '#8c6400', '#8e0000', '#f200f7', '#8b008c', '#005e90', '#05dcd0', '#0bf800', '#006f00', '#000000', '#d8d8d8', '#d8d8f6', '#0000f8', '#000066', '#f70077', '#010000')
ramsdis_ir_12bit = Colormap(colors=_ramsdis_ir_12bit_colors, controls=_ramsdis_ir_12bit_control_points)
_ramsdis_wv_12bit_control_points = (0.0, 0.0761904761904762, 0.07765567765567766, 0.07936507936507936, 0.3474969474969475, 0.34798534798534797, 0.39023199023199023, 0.3934065934065934, 0.43614163614163615, 0.43907203907203907, 0.4818070818070818, 0.4822954822954823, 0.48473748473748474, 0.6156288156288157, 0.6161172161172161, 0.64004884004884, 0.6405372405372405, 0.701098901098901, 0.7015873015873015, 0.7621489621489621, 0.7626373626373626, 0.8234432234432234, 0.8656898656898657, 0.8661782661782662, 0.8717948717948718, 0.8722832722832723, 0.884004884004884, 0.8844932844932845, 0.945054945054945, 0.9455433455433455, 1.0)
_ramsdis_wv_12bit_colors = ('#050500', '#313100', '#181800', '#000000', '#c8c800', '#fd4a4a', '#211212', '#4b0000', '#e20000', '#ff7e00', '#4b0000', '#430606', '#222222', '#ffffff', '#6496c8', '#4d7eb1', '#000064', '#0000fe', '#006400', '#00fe00', '#640000', '#ffff00', '#8a8a35', '#ffffff', '#ffffff', '#636347', '#4e4e50', '#ffffff', '#4e4e33', '#000031', '#000031')
ramsdis_wv_12bit = Colormap(colors=_ramsdis_wv_12bit_colors, controls=_ramsdis_wv_12bit_control_points)

white_trans = Colormap(colors=np.array([[0., 0., 0., 0.], [1., 1., 1., 1.]]))
red_trans = Colormap(colors=np.array([[0., 0., 0., 0.], [1., 0., 0., 1.]]))
green_trans = Colormap(colors=np.array([[0., 0., 0., 0.], [0., 1., 0., 1.]]))
blue_trans = Colormap(colors=np.array([[0., 0., 0., 0.], [0., 0., 1., 1.]]))

VIS_COLORMAPS = OrderedDict([
    ('CA (Low Light Vis)', ca_low_light_vis),
    ('Linear', linear),
    ('ZA', za_vis_default),
    ('Square Root (Vis Default)', SquareRootColormap()),
])

IR_COLORMAPS = OrderedDict([
    ('Rainbow (IR Default)', color11new),
    ('CIRA IR', cira_ir_default),
    ('Fog', fog),
    ('IR WV', ir_wv),
])

LIFTED_INDEX_COLORMAPS = OrderedDict([
    ('Lifted Index (New CIMSS)', lifted_index__new_cimss_table),
    ('Lifted Index', lifted_index_default),
])

PRECIP_COLORMAPS = OrderedDict([
    ('Blended TPW', blended_total_precip_water),
    ('Percent of Normal TPW', percent_of_normal_tpw),
    ('Precipitable Water (New CIMSS)', precip_water__new_cimss_table),
    ('Precipitable Water (Polar)', precip_water__polar),
    ('Precipitable Water', precip_water_default),
])

SKIN_TEMP_COLORMAPS = OrderedDict([
    ('Skin Temp (New CIMSS)', skin_temp__new_cimss_table),
    ('Skin Temp', skin_temp_default),
])

WV_COLORMAPS = OrderedDict([
    ('Gray Scale Water Vapor', gray_scale_water_vapor),
    ('NSSL VAS (WV Alternate)', nssl_vas_wv_alternate),
    ('RAMSDIS WV', ramsdis_wv),
    ('SLC WV', slc_wv),
])

TOWRS_COLORMAPS = OrderedDict([
    ('ACTP', actp),
    ('ADP', adp),
    ('RRQPE', rrqpe),
    ('VTRSB', vtrsb),
    ('CAPE', colorhcapeh10),
    ('LI', colorhlih10),
    ('PW10', colorhpw10h10),
    ('PW8', colorhpw8h10),
    ('IR Color Clouds Summer', ir_color_clouds_summer),
    ('IR Color Clouds Winter', ir_color_clouds_winter),
    ('WV Dry Yellow', wv_dry_yellow),
    ('Dust and Moisture Split', dust_and_moisture_split_window),
    ('Enhanced Rainbow', enhancedhrainbowh11),
    ('Enhanced RB Warmer Yellow', enhancedhrainbow_warmer_yellow),
    ('Fire Detection', fire_detection_3p9),
    ('RAMSDIS IR', ramsdis_ir_12bit),
    ('RAMSDIS WV', ramsdis_wv_12bit),
])

OTHER_COLORMAPS = OrderedDict([
    ('Rain Rate', rain_rate),
    ('Low Cloud Base', low_cloud_base),
    ('Cloud Amount', cloud_amount_default),
    ('Cloud Top Height', cloud_top_height),
    ('White Transparency', white_trans),
    ('Red Transparency', red_trans),
    ('Green Transparency', green_trans),
    ('Blue Transparency', blue_trans),
    ('grays', _colormaps['grays']),
])

ALL_COLORMAPS = {}
ALL_COLORMAPS.update(_colormaps)  # vispy's colormaps
ALL_COLORMAPS.update(VIS_COLORMAPS)
ALL_COLORMAPS.update(IR_COLORMAPS)
ALL_COLORMAPS.update(LIFTED_INDEX_COLORMAPS)
ALL_COLORMAPS.update(PRECIP_COLORMAPS)
ALL_COLORMAPS.update(SKIN_TEMP_COLORMAPS)
ALL_COLORMAPS.update(WV_COLORMAPS)
ALL_COLORMAPS.update(TOWRS_COLORMAPS)
ALL_COLORMAPS.update(OTHER_COLORMAPS)

CATEGORIZED_COLORMAPS = OrderedDict([
    ("Visible", VIS_COLORMAPS),
    ("IR", IR_COLORMAPS),
    ("Lifted Index", LIFTED_INDEX_COLORMAPS),
    ("Precipitable Water", PRECIP_COLORMAPS),
    ("Skin Temperature", SKIN_TEMP_COLORMAPS),
    ("Water Vapor", WV_COLORMAPS),
    ("TOWR-S", TOWRS_COLORMAPS),
    ("Other", OTHER_COLORMAPS),
])

DEFAULT_UNKNOWN = "grays"
DEFAULT_VIS = "Square Root (Vis Default)"
DEFAULT_IR = "Rainbow (IR Default)"
