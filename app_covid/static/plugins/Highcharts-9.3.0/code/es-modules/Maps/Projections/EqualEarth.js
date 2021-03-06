/* *
 *
 * Equal Earth projection, an equal-area projection designed to minimize
 * distortion and remain pleasing to the eye.
 *
 * Invented by Bojan Šavrič, Bernhard Jenny, and Tom Patterson in 2018. It is
 * inspired by the widely used Robinson projection.
 *
 * */
'use strict';
var A1 = 1.340264, A2 = -0.081106, A3 = 0.000893, A4 = 0.003796, M = Math.sqrt(3) / 2.0;
var EqualEarth = {
    forward: function (lonLat) {
        var d = Math.PI / 180, paramLat = Math.asin(M * Math.sin(lonLat[1] * d)), paramLatSq = paramLat * paramLat, paramLatPow6 = paramLatSq * paramLatSq * paramLatSq;
        var x = lonLat[0] * d * Math.cos(paramLat) / (M *
            (A1 +
                3 * A2 * paramLatSq +
                paramLatPow6 * (7 * A3 + 9 * A4 * paramLatSq)));
        var y = paramLat * (A1 + A2 * paramLatSq + paramLatPow6 * (A3 + A4 * paramLatSq));
        return [x, y];
    },
    inverse: function (xy) {
        var d = 180 / Math.PI, epsilon = 1e-9, iterations = 12;
        var paramLat = xy[1], paramLatSq, paramLatPow6, fy, fpy, dlat, i;
        for (i = 0; i < iterations; ++i) {
            paramLatSq = paramLat * paramLat;
            paramLatPow6 = paramLatSq * paramLatSq * paramLatSq;
            fy = paramLat * (A1 + A2 * paramLatSq + paramLatPow6 * (A3 + A4 * paramLatSq)) - xy[1];
            fpy = A1 + 3 * A2 * paramLatSq + paramLatPow6 * (7 * A3 + 9 * A4 * paramLatSq);
            paramLat -= dlat = fy / fpy;
            if (Math.abs(dlat) < epsilon) {
                break;
            }
        }
        paramLatSq = paramLat * paramLat;
        paramLatPow6 = paramLatSq * paramLatSq * paramLatSq;
        var lon = d * M * xy[0] * (A1 + 3 * A2 * paramLatSq + paramLatPow6 * (7 * A3 + 9 * A4 * paramLatSq)) / Math.cos(paramLat);
        var lat = d * Math.asin(Math.sin(paramLat) / M);
        return [lon, lat];
    }
};
export default EqualEarth;
