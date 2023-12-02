// forecast/static/forecast/js/pollJS.js

$(function () {
    updateChartWidths(); // 차트 업뎃
    console.log('Document ready');
    
    $('.choice').click(function () {
      console.log('Choice clicked');
      $('.choice').off('click');
      var choiceId = $(this).data('choice-id');
      var voteUrl = baseUrl;

      $.ajax({
          type: 'POST',
          url: voteUrl,
          data: { 'choice_id': choiceId, csrfmiddlewaretoken: '{{ csrf_token }}' },
          success: function (data) {
              console.log('AJAX success:', data);

              // 투표 .vote-count에 업뎃
              var choiceElement = $('.choice[data-choice-id=' + choiceId + ']');
              choiceElement.find('.vote-count').text(data.votes);

              // 차트 업뎃
              updateChartWidths();
          }
      });
  });
    

    function updateChartWidths() {
        var totalVotes = 0;
        $('.choice').each(function () {
            totalVotes += parseInt($(this).find('.vote-count').text());
        });

        // 차트 길이랑 퍼센트 계산 후 변화
        $('.choice').each(function () {
            var votes = parseInt($(this).find('.vote-count').text());
            var percentage = (votes / totalVotes) * 100;
            $(this).find('.chart').css('width', percentage + '%');
            $(this).find('.percentage-count').text(percentage.toFixed(2) + '%');
        });
    }
});
