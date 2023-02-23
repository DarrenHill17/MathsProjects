def calculate_q_codes(compass_heading: float, magnetic_variation: float, magnetic_deviation: float, relative_bearing: float) -> tuple:
    '''Calculate the Q Codes for a given compass heading and relative bearing, such as with an ADF'''
    output = [0, 0, 0, 0] # [QDM, QDR, QUJ, QTE]

    # Calculate magnetic heading by correcting for compass deviation
    magnetic_heading = compass_heading + magnetic_deviation

    # Calculate true heading by correction for variation at the aircraft's position
    true_heading = compass_heading + magnetic_variation + magnetic_deviation

    # QDM
    output[0] = magnetic_heading + relative_bearing

    # QDR
    output[1] = magnetic_heading + relative_bearing + 180

    # QUJ
    output[2] = true_heading + relative_bearing

    # QTE
    output[3] = true_heading + relative_bearing + 180

    # Normalise headings to be in range (0, 360]
    for i in range(len(output)):
        if output[i] <= 0:
            while output[i] <= 0:
                output[i] += 360
        elif output[i] > 360:
            while output[i] > 360:
                output[i] -= 360
    
    # String output to console
    qdm = str(output[0]).rjust(3, '0') + '°'
    qdr = str(output[1]).rjust(3, '0') + '°'
    quj = str(output[2]).rjust(3, '0') + '°'
    qte = str(output[3]).rjust(3, '0') + '°'
    print(f'QDM: {qdm}\nQDR: {qdr}\nQUJ: {quj}\nQTE: {qte}')

    return (qdm, qdr, quj, qte)

calculate_q_codes(310, -15, 0, 290)
