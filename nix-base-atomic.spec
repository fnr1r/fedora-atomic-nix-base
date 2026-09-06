Name:       nix-base-atomic
Version:    1
Release:    1
Summary:    Adds /nix directory
License:    MIT

%description
Just adds /nix, required to install Nix on atomic distros.

%install
mkdir -p %{buildroot}/nix

%files
/nix
