from conans import ConanFile, CMake, tools
import os

class TslOrderedMapConan(ConanFile):
    name = "tsl-ordered-map"
    version = "0.8.1"
    license = "MIT"
    description = "C++ hash map and hash set which preserve the order of insertion."
    homepage = "https://github.com/Tessil/ordered-map"
    url = "https://github.com/Tessil/conan-tsl-ordered-map"
    exports = "LICENSE"

    def source(self):
        tools.get("%s/archive/v%s.tar.gz" % (self.homepage, self.version))

    def package(self):
        self.copy("LICENSE", dst="licenses", keep_path=False, ignore_case=True)
        
        cmake = CMake(self)
        cmake.configure(source_folder="ordered-map-%s" % (self.version))
        cmake.install()

    def package_id(self):
        self.info.header_only()
