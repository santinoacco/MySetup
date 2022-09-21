# RUCIO

## Renew GRID certificates

1.  Choose a browser, I recommend firefox.
2.  Add to the browser the CERN certificates,
    download the 2 files from [this link](https://cafiles.cern.ch/cafiles/certificates/list.aspx?ca=grid) following the instructions for the browser.
3.  Install the downloaded files in the browser ([Mozilla](https://ca.cern.ch/ca/Help/?kbid=040110;040111&mode=print)):
    1.  <browser_settings>/.../<manage_certificates>
    2.  Under Authorities upload/install the files.
4.  Create a new certificate [here](https://ca.cern.ch/ca/) under `New Grid User Certificate`:
    1.  create a passphrase and verify it.
    2.  download the .p12 file and move it to your $HOME in afs/.
5.  @lxplus in your /afs/ dir, extract the certificate following [this](https://ca.cern.ch/ca/Help/?kbid=024010;024020;024100&mode=print) instructions; note that old certificates should be renamed to avoid conflicts.. later you can delete them.
6.  In addition you can add the certificate to the browser like you did with the other CERN certificates, but in this case you need to go to `My Certificates` and install your personal certificate.p12.

- official Twikis:

## Upload dataset

to find your RSE I went to my RucioUI and check the default RSEs were previous jobs were stored.

# PANDA

- official Twikis:

## `prun` for Python Jobs.



