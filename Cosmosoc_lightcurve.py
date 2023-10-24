import numpy as np
from astropy.io import fits
fits_image_filename = 'D:/IIT Dh/Cosmosoc/lightcurve_1.fits'
with fits.open(fits_image_filename) as hduI:
    hduI.info()
    table_data = hduI[1].columns
    print(table_data)
    image_data = hduI[2].data
    print(image_data)
    import matplotlib.pyplot as plt

    # CONTINUOS PLOT
    time = hduI[1].data['TIME']
    flux = hduI[1].data['PDCSAP_FLUX']
    sap = hduI[1].data['SAP_QUALITY']
    fig, ax = plt.subplots()
    ax.plot(time, flux, 'k')
    where_gt = np.where(sap>0)
    ax.plot(time[where_gt], flux[where_gt],'r')
    ax.set_ylabel('PSCSAP + SAP QUALITY ')
    ax.set_xlabel('TIME')
    ax.set_xlim(2900,2990)
    plt.title('  PSCSAP VS TIME whenever SAP QUALITY is > 0')
    plt.show()

    plt.figure()
    plt.imshow(image_data, cmap='magma' , origin='lower')
    plt.colorbar()
    plt.show()

    # DISCRETE PLOT
    time = hduI[1].data['TIME']
    flux = hduI[1].data['PDCSAP_FLUX']
    sap = hduI[1].data['SAP_QUALITY']
    fig, ax = plt.subplots()
    ax.plot(time, flux, 'ko')
    where_gt = np.where(sap > 0)
    ax.plot(time[where_gt], flux[where_gt], 'ro')
    ax.set_ylabel('PSCSAP + SAP QUALITY ')
    ax.set_xlabel('TIME')
    ax.set_xlim(2900, 2990)
    plt.title('  PSCSAP VS TIME whenever SAP QUALITY is > 0')
    plt.show()

