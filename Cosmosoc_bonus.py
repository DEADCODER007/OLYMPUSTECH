from astropy.io import fits
fits_image_filename = 'D:/IIT Dh/Cosmosoc/bonus_image_1.fits'
with fits.open(fits_image_filename) as hdul:
    hdul.info()
    image_data = hdul[0].data
    print(image_data)

    import matplotlib.pyplot as plt
    plt.figure()
    plt.imshow(image_data, cmap='ocean', origin='lower')
    plt.colorbar()
    plt.show()

    # info on data
    col = hdul[1].columns
    print(col)

    # ETA vs XI
    x = hdul[1].data['XI']
    print(x)
    y = hdul[1].data['ETA']
    fig, ax = plt.subplots()
    ax.plot(x, y, 'r')
    ax.set_xlabel('XI')
    ax.set_ylabel('ETA')
    fig.suptitle(" ETA vs XI")
    plt.show()

    # ETA_CORR VS XI
    x = hdul[1].data['XI']
    print(x)
    y = hdul[1].data['ETA_CORR']
    fig, ax = plt.subplots()
    ax.plot(x, y,'ko')
    ax.set_xlabel('XI')
    ax.set_ylabel('ETA_CORR')
    fig.suptitle(" ETA_CORR vs XI")
    plt.show()

    #ETA_CORR VS ETA
    x = hdul[1].data['ETA']
    print(x)
    y = hdul[1].data['ETA_CORR']
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('ETA')
    ax.set_ylabel('ETA_CORR')
    fig.suptitle(" ETA_CORR vs ETA")
    plt.show()




