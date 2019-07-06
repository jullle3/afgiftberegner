# statistik udtræk af DMR ftp://dmr-ftp-user:dmrpassword@5.44.137.84/ESStatistikListeModtag/


def beregn_billig_afgift(pris_uden_afgift, varebil):
    return pris_uden_afgift * 0.85


def beregn_dyr_afgift(pris_uden_afgift, varebil):
    nedre_afgift = 193400 * 0.85
    øvre_afgift = (pris_uden_afgift - 193400) * 1.5
    return nedre_afgift + øvre_afgift


def beregn(pris_uden_afgift, varebil=False):
    afgift = 0
    """
    Fra skat.dk D.6/7/2019 under Personbiler:
    85 % af afgiftsværdien op til 193.400 og 150 % af resten i 2019.
    """

    # TODO: Tilføj alle fradrag/tillæg grundet motorstørelser, motortype, sikkerhed m.m.
    if 193400 >= pris_uden_afgift:
        afgift = beregn_billig_afgift(pris_uden_afgift, varebil)
    elif pris_uden_afgift > 193400:
        afgift = beregn_dyr_afgift(pris_uden_afgift, varebil)
    else:
        print(f"ERROR: Prisen {pris_uden_afgift} er ugyldig")

    print(f'Uden afgift: {pris_uden_afgift} kr\nAfgift: {int(afgift)} kr\nTotal: {int(pris_uden_afgift + afgift)} kr\nAfgift udgør: {afgift/pris_uden_afgift*100:.4}%')
if __name__ == "__main__":
    beregn(200000)