set of int: MenuVersions = {150, 140, 130, 120, 110, 100};
set of int: DropdownVersions = {230, 220, 210, 200, 180};
set of int: IconVersions = {200, 100};

var MenuVersions: selected_menu;
var DropdownVersions: selected_dropdown;
var IconVersions: selected_icons;

constraint
    (selected_icons = 100) 
    /\
    (selected_menu = 100 -> selected_dropdown = 180) 
    /\
    ((selected_menu >= 110 /\ selected_menu <= 150) ->  (selected_dropdown >= 200 /\ selected_dropdown <= 230))
    /\
    ((selected_dropdown  >= 200 /\ selected_dropdown <= 230) ->
    (selected_icons = 200));

solve satisfy;

output [
    "Selected menu version: \(selected_menu)\n",
    "Selected dropdown version: \(selected_dropdown)\n",
    "Selected icon version: \(selected_icons)\n"
];
