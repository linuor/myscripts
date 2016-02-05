import QtQuick 2.3
import QtQuick.Controls 1.2

MenuBar {
    Menu {
        title: qsTr("File")
        MenuItem {
            text: qsTr("&Open")
            onTriggered: console.log("Open action triggered");
        }
        MenuItem {
            text: qsTr("2Exit")
            onTriggered: Qt.quit();
        }
    }
}
