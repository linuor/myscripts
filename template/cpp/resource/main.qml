import QtQuick 2.3
import QtQuick.Controls 1.2

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")

    menuBar: MainMenu {}
    Label {
        text: qsTr("Hello World")
        anchors.centerIn: parent
    }
}
