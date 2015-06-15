$(document).ready(function() {
  $('select').chosen();
      $('.btn-file :file').on('fileselect', function(event, numFiles, label) {
        console.log(numFiles);
        console.log(label);
    });
});