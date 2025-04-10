import ROOT

RHIST = {1: ROOT.TH1F, 2: ROOT.TH2F, 3: ROOT.TH3F, 4: ROOT.THnF}

class rhist:
    def __init__(self, name: str, title: str, *bin_specs: list):
        """Create ROOT histogram from standard bin specifications or arrays"""
        self.hist = None

        var_bins = [hasattr(spec, "__len__") for spec in bin_specs]
        assert all(var_bins) or not any(var_bins), f"either all bins must be variable or fixed width: {bin_specs=}"

        dim = len(bin_specs) if all(var_bins) else len(bin_specs) / 3
        assert int(dim) == dim and dim > 0, "dimension must be positive and integral"
        print(f"{dim=}")

        if all(var_bins):
            nbins = list(map(lambda a: len(a) - 1, bin_specs))

        if dim <= 3:
            if all(var_bins):
                bin_defs = zip(nbins, bin_specs)
                bin_specs = [arg for axis in bin_defs for arg in axis]
            print("here")
            self.hist = RHIST[min(dim, 4)](name, title, *bin_specs)
        elif all(var_bins):
            nbins = np.asarray(nbins, "i")
            self.hist = RHIST[min(dim, 4)](name, title, dim, nbins, bin_specs)
        else:
            raise NotImplementedError

    # use properties instead?

    def dim():
        return 0

    def axes():
        return []

    def axis(self, iaxis: int):
        return None

    def project():
        pass

    def fill():
        pass

    def no_bins():
        return 0
