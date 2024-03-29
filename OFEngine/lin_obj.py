# Copyright (c) 2023, Md Imam Hossain (emamhd at gmail dot com)
# see LICENSE.txt for details

# Linux gcc libraries
LIN_GCC_LIBS_DEPS = ('libasan.so', 'libatomic.so', 'libgcc_s.so', 'libgdruntime.so', 'libgfortran.so', 'libgo.so', 'libgomp.so', 'libgphobos.so', 'libitm.so', 'liblsan.so', 'libobjc.so', 'libquadmath.so', 'libstdc++.so', 'libtsan.so', 'libubsan.so')

# Linux gcc core libraries
LIN_GCC_CR_DEPS = ('libanl.so', 'libc.so', 'libdl.so', 'libm.so', 'libmemusage.so', 'libmvec.so', 'libnsl.so', 'libnss_compat.so', 'libnss_db.so', 'libnss_dns.so', 'libnss_files.so', 'libnss_hesiod.so', 'libpcprofile.so', 'libpthread.so', 'libresolv.so', 'librt.so', 'libthread_db.so', 'libutil.so', )

# Linux core libraries
LIN_CR_DEPS = ('linux-vdso.so', 'linux-gate.so', 'libstdc++.so.6', 'libstdc++.so.5', 'ld-linux-x86-64.so.2', 'libstdc++-libc6.2-2.so.3')

# Linux network and system support libraries
LIN_STD_LV1_DEPS = ('libdatrie.so.1', 'libfribidi.so.0', 'libsqlite3.so.0', 'libheimbase.so.1', 'libtasn1.so.6', 'libkeyutils.so.1', 'libblkid.so.1', 'libpcre2-8.so.0', 'libgmp.so.10', 'libnettle.so.8', 'libunistring.so.2', 'libkrb5support.so.0', 'libcom_err.so.2', 'libsasl2.so.2', 'libffi.so.8', 'liblber-2.4.so.2', 'libnghttp2.so.14', 'libdb-5.3.so', 'libgomp.so.1', 'libcrypto.so.1.1', 'libcrypto.so.1.0.0', 'libluajit-5.1.so.2', 'libpcre.so.3', 'libslang.so.2', 'libgpg-error.so.0', 'liblzma.so.5', 'libcap-ng.so.0', 'libtinfo.so.5', 'libtinfo.so.6', 'libnspr4.so', 'libutil.so.1', 'libuuid.so.1', 'liblz4.so.1', 'libzstd.so.1', 'libcrypt.so.1', 'libexpat.so.1', 'libz.so.1', 'libbsd.so.0', 'libdrm.so.2')

LIN_STD_DEPS = ( 'libhx509.so.5', 'libwind.so.0', 'libroken.so.18', 'libhcrypto.so.4', 'libasn1.so.8', 'libkrb5.so.26', 'libheimntlm.so.0', 'libp11-kit.so.0', 'libhogweed.so.6', 'libk5crypto.so.3', 'libkrb5.so.3', 'libgnutls.so.30', 'libgssapi.so.3', 'libldap_r-2.4.so.2', 'libgssapi_krb5.so.2', 'libpsl.so.5', 'libssh.so.4', 'librtmp.so.1', 'libidn2.so.0', 'libselinux.so.1', 'libmount.so.1', 'libplc4.so', 'libplds4.so', 'libreadline.so.8', 'libgmodule-2.0.so.0', 'libnss3.so', 'libnssutil3.so', 'libsmime3.so', 'libpcap.so.0.8', 'libssl.so.1.1', 'libgio-2.0.so.0', 'libcurl.so.4', 'libgobject-2.0.so.0', 'libglib-2.0.so.0', 'libncursesw.so.6', 'libdbus-1.so.3', 'libgcrypt.so.20', 'libncurses.so.5', 'libaudit.so.1', 'libpam.so.0', 'libsystemd.so.0', 'libgbm.so.1')

# Linux graphics libraries
LIN_GRA_DEPS = ('liblcms2.so.2', 'libgdk-3.so.0', 'libgtk-3.so.0', 'libcaca.so.0', 'libfreetype.so.6', 'libxcb-render.so.0', 'libxcb-shm.so.0', 'libfontconfig.so.1', 'libX11.so.6', 'libGL.so.1', 'libGLU.so.1', 'libxcb.so.1', 'libGLX.so.0', 'libGLdispatch.so.0', 'libvulkan.so.1', 'libXdmcp.so.6', 'libXau.so.6', 'libXfixes.so.3', 'libXrender.so.1', 'libxkbcommon.so.0', 'libXxf86vm.so.1', 'libXss.so.1', 'libXrandr.so.2', 'libXi.so.6', 'libXinerama.so.1', 'libXcursor.so.1', 'libXext.so.6', 'libXt.so.6', 'libXmu.so.6', 'libICE.so.6', 'libSM.so.6', 'libgdk_pixbuf-2.0.so.0', 'libgtk-x11-2.0.so.0', 'libepoxy.so.0', 'libglut.so.3 ', 'libGLEW.so.1.5', 'libpangocairo-1.0.so.0', 'libpango-1.0.so.0', 'libXcomposite.so.1', 'libX11-xcb.so.1', 'libXdamage.so.1', 'libXtst.so.6', 'libwayland-egl.so.1', 'libwayland-client.so.0', 'libwayland-cursor.so.0', 'libcairo-gobject.so.2', 'libatk-1.0.so.0', 'libatk-bridge-2.0.so.0', 'libpangoft2-1.0.so.0', 'libharfbuzz.so.0', 'libgdk-x11-2.0.so.0', 'libthai.so.0', 'libatspi.so.0', 'libgraphite2.so.3', 'libttf.so.2')

# Linux audio libraries
LIN_AU_DEPS = ('libasound.so.2', 'libpulse-simple.so.0', 'libpulse.so.0')

# Linux multimedia support libraries
LIN_ML_DEPS = ('libSDL_ttf-2.0.so.0', 'libSDL_image-1.2.so.0', 'libSDL2_image-2.0.so.0', 'libSDL2_net-2.0.so.0', 'libSDL2-2.0.so.0', 'libSDL_mixer-1.2.so.0', 'libSDL-1.2.so.0', 'libvorbisfile.so.3', 'libphysfs.so.1', 'libopenal.so.0', 'libopenal.so.1', 'libmodplug.so.1', 'libvorbis.so.0', 'libtheoradec.so.1', 'libogg.so.0', 'libmpg123.so.0', 'libsndfile.so.1', 'libvorbisenc.so.2', 'libtheora.so.0', 'libIL.so.1', 'libbrotlidec.so.1', 'libbrotlicommon.so.1', 'libcairo.so.2', 'libpixman-1.so.0', 'libfreeimage.so.3', 'libalut.so.0', 'libILU.so.1', 'libpng12.so.0', 'libtiff.so.3', 'libmng.so.1', 'libjpeg.so.62', 'libxerces-c.so.27', 'libjpeg.so.8', 'libsamplerate.so.0', 'libpng16.so.16', 'libtiff.so.5', 'libwebp.so.6', 'libmikmod.so.3', 'libfluidsynth.so.2', 'libFLAC.so.8', 'libmad.so.0', 'libsndio.so.7.0', 'libjxrglue.so.0', 'libopenjp2.so.7', 'libraw.so.19', 'libwebpmux.so.3', 'libIlmImf-2_5.so.25', 'libHalf-2_5.so.25', 'libIex-2_5.so.25', 'libjbig.so.0', 'libjack.so.0', 'libinstpatch-1.0.so.2', 'libjpegxr.so.0', 'libImath-2_5.so.25', 'libIlmThread-2_5.so.25', 'libSDL-1.1.so.0', 'libsmpeg-0.4.so.0', 'libSDL_mixer-1.0.so.0')