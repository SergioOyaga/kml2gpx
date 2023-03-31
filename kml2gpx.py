import sys
import fastkml
import gpxpy.gpx
import pygeoif
from tkinter.filedialog import askopenfilename


def write_string(string):
    return string


def add_track_to_gpx(feature, gpx_obj):
    # Create first track in our GPX:
    gpx_track = gpx_obj.tracks[0]

    # Create first segment in our GPX track:
    gpx_segment = gpxpy.gpx.GPXTrackSegment()

    # Create points:
    for coord in feature.geometry.coords:
        gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(coord[1], coord[0]))

    # Append segment to track and track to gpx
    gpx_track.segments.append(gpx_segment)


def add_waypoint_to_gpx(feature, gpx_obj, mapping):
    gpx_wps = gpxpy.gpx.GPXWaypoint()
    gpx_wps.latitude = feature.geometry.coords[0][1]
    gpx_wps.longitude = feature.geometry.coords[0][0]
    symbol = mapping.get(feature.styleUrl.removeprefix('#'), '')
    if symbol != '':
        gpx_wps.symbol = symbol
    gpx_wps.name = write_string(feature.name)
    gpx_wps.description = write_string("Waypoint")
    gpx_obj.waypoints.append(gpx_wps)


def parse_place_marks(element, mapping, gpx_obj, route_name):
    bool_idx = True
    for feature in element.features():
        if isinstance(feature, fastkml.kml.Placemark):
            if isinstance(feature.geometry, pygeoif.geometry.LineString):
                if bool_idx:
                    track = gpxpy.gpx.GPXTrack()
                    track.name = write_string(route_name)
                    gpx_obj.tracks.append(track)
                    bool_idx = False
                # add track to gpx
                add_track_to_gpx(feature, gpx_obj)
            elif isinstance(feature.geometry, pygeoif.geometry.Point):
                # add waypoint to gpx
                add_waypoint_to_gpx(feature, gpx_obj, mapping)
    for feature in element.features():
        if isinstance(feature, fastkml.kml.Folder) or isinstance(feature, fastkml.kml.Document):
            parse_place_marks(feature, mapping, gpx_obj, route_name)


def get_style_relations(styles_list):
    maps = []
    styles = []
    mapping = {}
    for style in styles_list:
        if isinstance(style, fastkml.kml.Style):
            styles.append(style)
        elif isinstance(style, fastkml.kml.StyleMap):
            maps.append(style)
    for map_obj in maps:
        for sty in styles:
            if map_obj.normal.url.endswith(sty.id) and sty._styles[0].icon_href is not None:
                mapping[map_obj.id] = ''.join(sty._styles[0].icon_href.partition('CUSTOM')[1:]).removesuffix('.png')
    return mapping


if __name__ == '__main__':
    # Input KML file
    kml_file = askopenfilename()
    if not kml_file.endswith('.kml'):
        sys.exit("No .kml selected")

    # Read inpt file
    with open(kml_file, 'rb') as my_file:
        doc = my_file.read()
    
    # Create KML object
    k = fastkml.kml.KML()
    k.from_string(doc)
    
    # Create dictionary to relate Styles of icons with the real icon Names
    style_map = get_style_relations(list(list(k.features())[0].styles()))
    
    # Create a new GPX file
    gpx = gpxpy.gpx.GPX()

    # Parse PlaceMarks to GPX format
    parse_place_marks(k, style_map, gpx, list(k.features())[0].name.removesuffix('.kml'))
    
    # Save GPX file
    gpx_file = kml_file.removesuffix('kml')+'gpx'
    f = open(gpx_file, 'wb')
    f.write(gpx.to_xml().encode('utf8'))
    f.close()
