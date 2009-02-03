function run_show(show_frame, data) {
    // Show the data in show_frame
    show_frame.location.href = data[0]['fields']['url'];
}