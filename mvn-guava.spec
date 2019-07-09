#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-guava
Version  : 14.0.1
Release  : 5
URL      : https://repo1.maven.org/maven2/com/google/guava/guava/14.0.1/guava-14.0.1.jar
Source0  : https://repo1.maven.org/maven2/com/google/guava/guava/14.0.1/guava-14.0.1.jar
Source1  : https://repo1.maven.org/maven2/com/google/guava/guava-parent/14.0.1/guava-parent-14.0.1.pom
Source2  : https://repo1.maven.org/maven2/com/google/guava/guava-parent/19.0/guava-parent-19.0.pom
Source3  : https://repo1.maven.org/maven2/com/google/guava/guava-parent/25.1-android/guava-parent-25.1-android.pom
Source4  : https://repo1.maven.org/maven2/com/google/guava/guava/11.0.2/guava-11.0.2.jar
Source5  : https://repo1.maven.org/maven2/com/google/guava/guava/11.0.2/guava-11.0.2.pom
Source6  : https://repo1.maven.org/maven2/com/google/guava/guava/14.0.1/guava-14.0.1.pom
Source7  : https://repo1.maven.org/maven2/com/google/guava/guava/19.0/guava-19.0.jar
Source8  : https://repo1.maven.org/maven2/com/google/guava/guava/19.0/guava-19.0.pom
Source9  : https://repo1.maven.org/maven2/com/google/guava/guava/25.1-android/guava-25.1-android.jar
Source10  : https://repo1.maven.org/maven2/com/google/guava/guava/25.1-android/guava-25.1-android.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-guava-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-guava package.
Group: Data

%description data
data components for the mvn-guava package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/guava/guava/14.0.1
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/com/google/guava/guava/14.0.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/guava/guava-parent/14.0.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/google/guava/guava-parent/14.0.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/guava/guava-parent/19.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/google/guava/guava-parent/19.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/guava/guava-parent/25.1-android
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/google/guava/guava-parent/25.1-android

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/guava/guava/11.0.2
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/com/google/guava/guava/11.0.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/guava/guava/11.0.2
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/com/google/guava/guava/11.0.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/guava/guava/14.0.1
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/com/google/guava/guava/14.0.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/guava/guava/19.0
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/com/google/guava/guava/19.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/guava/guava/19.0
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/com/google/guava/guava/19.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/guava/guava/25.1-android
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/com/google/guava/guava/25.1-android

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/guava/guava/25.1-android
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/com/google/guava/guava/25.1-android


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/google/guava/guava-parent/14.0.1/guava-parent-14.0.1.pom
/usr/share/java/.m2/repository/com/google/guava/guava-parent/19.0/guava-parent-19.0.pom
/usr/share/java/.m2/repository/com/google/guava/guava-parent/25.1-android/guava-parent-25.1-android.pom
/usr/share/java/.m2/repository/com/google/guava/guava/11.0.2/guava-11.0.2.jar
/usr/share/java/.m2/repository/com/google/guava/guava/11.0.2/guava-11.0.2.pom
/usr/share/java/.m2/repository/com/google/guava/guava/14.0.1/guava-14.0.1.jar
/usr/share/java/.m2/repository/com/google/guava/guava/14.0.1/guava-14.0.1.pom
/usr/share/java/.m2/repository/com/google/guava/guava/19.0/guava-19.0.jar
/usr/share/java/.m2/repository/com/google/guava/guava/19.0/guava-19.0.pom
/usr/share/java/.m2/repository/com/google/guava/guava/25.1-android/guava-25.1-android.jar
/usr/share/java/.m2/repository/com/google/guava/guava/25.1-android/guava-25.1-android.pom
