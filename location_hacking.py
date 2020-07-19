# distance /= 6371009.0D;  //earth_radius = 6371009 # in meters
# heading = Math.toRadians(heading);
# double fromLat = Math.toRadians(from.latitude);
# double fromLng = Math.toRadians(from.longitude);
# double cosDistance = Math.cos(distance);
# double sinDistance = Math.sin(distance);
# double sinFromLat = Math.sin(fromLat);
# double cosFromLat = Math.cos(fromLat);
# double sinLat = cosDistance * sinFromLat + sinDistance * cosFromLat * Math.cos(heading);
# double dLng = Math.atan2(sinDistance * cosFromLat * Math.sin(heading), cosDistance - sinFromLat * sinLat);
# return new LatLng(Math.toDegrees(Math.asin(sinLat)), Math.toDegrees(fromLng + dLng));
import math


def convert_x_y_to_d_angle(x0, y0, x, y, lat_from, lon_from):
    x = x - x0
    y = y0-y
    d = math.sqrt(x**2 + y**2)
    angle = math.degrees(math.atan2(y, x))
    lat_lon=convert_metter_to_lat_lon(lat_from, lon_from, d/100, angle)
    return {
        'd': d,
        'angle': angle,
        'x': x,
        'y': y,
        'lat': lat_lon['lat'],
        'lon': lat_lon['lon']
    }


def convert_metter_to_lat_lon(lat_from, lon_from, distance, heading):
    distance /= 6371009
    heading = math.radians(heading)
    from_lat = math.radians(lat_from)
    from_lng = math.radians(lon_from)
    cos_distance = math.cos(distance)
    sin_distance = math.sin(distance)
    sin_from_lat = math.sin(from_lat)
    cos_from_lat = math.cos(from_lat)
    sin_lat = cos_distance*sin_from_lat + \
        sin_distance*cos_from_lat*math.cos(heading)
    d_lng = math.atan2(sin_distance*cos_from_lat *
                       math.sin(heading), cos_distance - sin_from_lat * sin_lat)
    return {
        'lat': math.degrees(math.asin(sin_lat)),
        'lon': math.degrees(from_lng + d_lng)
    }


if __name__ == "__main__":
    points = []
    start_location = convert_metter_to_lat_lon(10.7730073, 106.6595646, 0, 30)
    # point = convert_x_y_to_d_angle(493, 275, 775, 0, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 750, 16, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 725, 31, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 698, 60, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 666, 79, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 627, 86, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 626, 88, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 594, 103, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 575, 130, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 541, 143, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 509, 145, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 507, 156, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 512, 156, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 508, 170, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 503, 187, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 493, 204, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 495, 222, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 492, 240, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 490, 253, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 489, 258, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 487, 267, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 485, 281, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 484, 290, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 483, 295, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 485, 309, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 476, 323, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 487, 314, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 480, 304, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 481, 305, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 486, 297, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 486, 289, start_location['lat'],start_location['lon'])
    # points.append(point)
    # point = convert_x_y_to_d_angle(493, 275, 491, 286, start_location['lat'],start_location['lon'])
    # points.append(point)

    point = convert_x_y_to_d_angle(493, 275, 227, 498, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 248, 435, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 270, 427, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 283, 412, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 302, 405, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 329, 398, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 345, 381, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 362, 368, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 378, 354, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 392, 343, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 414, 337, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 479, 330, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 433, 329, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 450, 317, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 464, 303, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 472, 297, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 481, 294, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 498, 292, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 513, 272, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 551, 249, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 554, 257, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 551, 256, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 542, 257, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 536, 259, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 526, 263, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 516, 272, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 504, 278, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 493, 289, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 488, 287, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 477, 286, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 462, 290, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 448, 293, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 450, 289, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 448, 293, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 461, 282, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 467, 279, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 473, 272, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 476, 277, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 479, 279, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 475, 275, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 472, 282, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 475, 276, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 478, 282, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 481, 275, start_location['lat'],start_location['lon'])
    points.append(point)
    point = convert_x_y_to_d_angle(493, 275, 481, 281, start_location['lat'],start_location['lon'])
    points.append(point)

    lines = []
    for point in points:
        keys = point.keys()
        words = []
        for key in keys:
            words.append(str(point[key]))
        line = ','.join(words)
        lines.append(line)
    with open('./video/location.csv','w') as f:
        f.write('\n'.join(lines))