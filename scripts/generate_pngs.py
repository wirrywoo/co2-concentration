import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.basemap import Basemap
from osgeo import gdal

class CO2Visualizer:
    def __init__(self, tiff_root='./data/raw', output_dir='../static/images'):
        self.tiff_root = tiff_root
        self.output_dir = output_dir

    def process_data_directory(self):
        for directory_path, _, file_list in os.walk(self.tiff_root):
            for index, filename in enumerate(file_list):
                if not filename.endswith('.tif'):
                    continue
                self._process_tiff_file(directory_path, filename, index)

    def _process_tiff_file(self, directory_path, filename, index):
        _, date_string, _ = filename.split('.')
        year, _, _ = date_string.split('_')

        year_output_dir = os.path.join(os.path.dirname(directory_path), self.output_dir, year)
        os.makedirs(year_output_dir, exist_ok=True)
        output_filepath = os.path.join(year_output_dir, f"{index % 351 + 1}.png")

        raster_path = os.path.join(directory_path, filename)
        raster = gdal.Open(raster_path)
        raster_band = raster.GetRasterBand(1)

        raster_array = raster_band.ReadAsArray()
        masked_array = 1e6 * np.ma.masked_equal(raster_array, raster_band.GetNoDataValue())

        self._generate_plot(masked_array, output_filepath)

    def _generate_plot(self, data_array, output_filepath):
        with plt.style.context('ggplot'), mpl.rc_context({"text.usetex": True}):
            plt.figure(figsize=(15, 7.5))
            map_projection = Basemap(projection='cyl', resolution='c', lat_0=0, lon_0=0)

            flipped_data = np.flipud(data_array)
            rows, cols = flipped_data.shape
            longitudes, latitudes = map_projection.makegrid(cols, rows)
            x_coords, y_coords = map_projection(longitudes, latitudes)

            contour_levels = np.arange(390, 425.5, 0.5)
            contour = map_projection.contourf(x_coords, y_coords, flipped_data, levels=contour_levels, cmap=plt.cm.RdYlGn_r)

            colorbar = map_projection.colorbar(contour, location='bottom', pad='10%', label='\nParts per million (ppm)')
            colorbar.set_ticks([390, 395, 400, 405, 410, 415, 420, 425])

            map_projection.drawcoastlines(linewidth=0.5)
            map_projection.drawmeridians(np.arange(0, 360, 60), linewidth=0.2, labels=[1, 0, 0, 1], labelstyle='+/-', color='grey')
            map_projection.drawparallels(np.arange(-90, 90, 30), linewidth=0.2, labels=[1, 0, 0, 1], labelstyle='+/-', color='grey')
            map_projection.drawmapboundary(linewidth=0.5, color='grey')

            plt.savefig(output_filepath, pad_inches = 0, bbox_inches = 'tight')
            plt.close()

if __name__ == "__main__":
    visualizer = CO2Visualizer()
    visualizer.process_data_directory()